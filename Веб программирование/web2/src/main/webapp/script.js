"use strict";

let x, y, r;

let svg = document.getElementById("svg");

// Function to draw a point on the SVG
function drawPoint(x, y, r, result) {
  console.log(`Drawing point at (${x}, ${y}, ${r}) with result: ${result}`);
  let circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  circle.setAttribute("cx", x * 60 * 2 / r + 150);
  circle.setAttribute("cy", -y * 60 * 2 / r + 150);
  circle.setAttribute("r", 3);
  circle.style.fill = result ? "#09a53d" : "#a50909";
  svg.appendChild(circle);
}

// Function to transform SVG coordinates to plane coordinates
function transformSvgToPlane(svgX, svgY, r) {
  let planeX = (svgX - 150) / (120 / r);
  let planeY = (150 - svgY) / (120 / r);
  console.log(`Transformed SVG (${svgX}, ${svgY}) to plane (${planeX}, ${planeY})`);
  return { x: planeX, y: planeY };
}

// Function to add a point to the table
function addToTable(x, y, r, result) {
  console.log(`Adding point to table: (${x}, ${y}, ${r}) with result: ${result}`);
  const table = document.getElementById("outputTable");
  const span = document.getElementById("notifications");
  if (span) {
    span.innerText = "";
    span.className = "notification";
  }

  const newRow = table.insertRow();
  newRow.insertCell().innerText = x;
  newRow.insertCell().innerText = y;
  newRow.insertCell().innerText = r;
  newRow.insertCell().innerHTML = result
    ? "<span class=\"success\">Попал</span>"
    : "<span class=\"fail\">Промазал</span>";
}

// Function to send a point to the server and check if it hits the target
async function checkPoint(x, y, r) {
  console.log(`Sending point to server: (${x}, ${y}, ${r})`);
  const url = "controller";
  const params = new URLSearchParams({ X: x, Y: y, R: r, action: "checkPoint" });

  try {
    const response = await fetch(url + "?" + params.toString(), { method: "GET" });
    const data = await response.json();
    console.log("Received response from server:", data);
    return data.result; // Assuming 'result' is the key in the response JSON
  } catch (error) {
    console.error('Error:', error);
    createNotification("Не удалось отправить точку.");
    return null;
  }
}

// Function to create a notification message
function createNotification(message) {
  console.log("Creating notification:", message);
  let outputContainer = document.getElementById("outputContainer");
  if (outputContainer.contains(document.querySelector(".notification"))) {
    let stub = document.querySelector(".notification");
    stub.textContent = message;
    stub.classList.add("errorStub");
    if (stub.classList.contains("outputStub")) {
      stub.classList.remove("outputStub");
    }
  } else {
    let notificationTableRow = document.createElement("h4");
    notificationTableRow.innerHTML = "<span class='notification errorStub'></span>";
    outputContainer.prepend(notificationTableRow);
    let span = document.querySelector(".notification");
    span.textContent = message;
  }
}

// Function to validate the Y value
function validateY() {
  let selectedY = document.querySelector("input[name='Y-radio-group']:checked");

  if (selectedY) {
    y = parseFloat(selectedY.value);
    return true;
  } else {
    createNotification("Значение Y не выбрано");
    return false;
  }
}

// Function to validate the X value
function validateX() {
  x = document.querySelector("input[name='X-input']").value.replace(",", ".");
  if (x === undefined) {
    createNotification("X не введён");
    return false;
  } else if (!isNumeric(x)) {
    createNotification("X не число");
    return false;
  } else if (x < -5 || x > 3) {
    createNotification("X не входит в область допустимых значений");
    return false;
  } else return true;
}

// Function to validate the R value
function validateR() {
  r = document.querySelector("input[name='R-input']").value.replace(",", ".");
  if (r === undefined) {
    createNotification("R не введён");
    return false;
  } else if (!isNumeric(r)) {
    createNotification("R не число");
    return false;
  } else if (r < 1 || r > 4) {
    createNotification("R не входит в область допустимых значений");
    return false;
  } else return true;
}

// Function to check if a value is numeric
function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function prepareAndSendPoint(xValue, yValue, rValue) {
  x = parseFloat(xValue.toFixed(1));
  y = parseFloat(yValue);
  r = parseFloat(rValue);

  checkPoint(x, y, r).then(result => {
    if (result !== null) {
      drawPoint(x, y, r, result);
      addToTable(x, y, r, result);
    }
  }).catch(error => {
    console.error('Error while sending point:', error);
    createNotification("Error: Could not send the point");
  });
}

document.addEventListener("DOMContentLoaded", () => {

  svg.addEventListener("click", (event) => {
    if (validateR()) {
      let point = svg.createSVGPoint();
      point.x = event.clientX;
      point.y = event.clientY;

      let ctm = svg.getScreenCTM();
      if (ctm) {
        let invertedCTM = ctm.inverse();
        let svgPoint = point.matrixTransform(invertedCTM);

        let planeCoords = transformSvgToPlane(svgPoint.x, svgPoint.y, r);
        prepareAndSendPoint(planeCoords.x, planeCoords.y, r);
      }
    }
  });

  document.getElementById("checkButton").onclick = function () {
    if (validateX() && validateY() && validateR()) {
      prepareAndSendPoint(x, y, r);
    }
  };

  let buttons = document.querySelectorAll("input[name='X-button']");
  buttons.forEach(button => {
    button.onclick = function () {
      x = this.value;
      buttons.forEach(btn => {
        btn.style.boxShadow = null;
        btn.style.backgroundColor = null;
        btn.style.color = null;
      });
      this.style.boxShadow = "0 0 40px 5px #f41c52";
      this.style.backgroundColor = "#f41c52";
      this.style.color = "white";
    };
  });

  const xInput = document.querySelector("input[name='X-input']");
  const rInput = document.querySelector("input[name='R-input']");
  if (xInput) xInput.value = "0";
  if (rInput) rInput.value = "1";
});
