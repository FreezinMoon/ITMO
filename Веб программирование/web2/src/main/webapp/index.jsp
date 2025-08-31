<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="web.dao.PointDao" %>
<%@ page import="web.models.Point" %>
<%@ page import="java.util.List" %>

<!DOCTYPE html>
<html lang="ru-RU">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <meta name="author" content="Гуменник Петр Олегович">
  <meta name="description" content="Веб-программирование: Лабораторная работа №2.">
  <meta name="keywords" content="ITMO, ИТМО, ПИиКТ, ВТ, Лабораторная работа, Веб-программирование"/>

  <link href="stylesheets/styles.css" rel="stylesheet">
  <link rel="icon" type="image/jpg" href="images/favicon.jpg">
  <title>Лабораторная работа №2 | Веб-программирование</title>
</head>

<body>
<header class="shaded animated">
  <h1>Веб-программирование, Лабораторная работа №2, Вариант 999818</h1>
  <div id="credit">
    <a>
      Гуменник Петр Олегович, P3233
    </a>
  </div>
</header>

<table id="mainTable" class="shaded">
  <thead>
  <td colspan="5">
    <h3>Валидация введённых значений:</h3>
  </td>
  </thead>
  <tbody>
  <tr>
    <td colspan="5">
      <hr>
    </td>
  </tr>

  <tr>
    <td>Введите X:</td>
    <td colspan="3">
      <input required name="X-input" class="illuminated animated" type="text" placeholder="-5...3" maxlength="6">
    </td>
    <td rowspan="9">
      <svg xmlns="http://www.w3.org/2000/svg" id="svg">
        <line x1="0" y1="150" x2="300" y2="150" stroke="#000720"></line>
        <line x1="150" y1="0" x2="150" y2="300" stroke="#000720"></line>
        <line x1="270" y1="148" x2="270" y2="152" stroke="#000720"></line>
        <text x="265" y="140">R</text>
        <line x1="210" y1="148" x2="210" y2="152" stroke="#000720"></line>
        <text x="200" y="140">R/2</text>
        <line x1="90" y1="148" x2="90" y2="152" stroke="#000720"></line>
        <text x="75" y="140">-R/2</text>
        <line x1="30" y1="148" x2="30" y2="152" stroke="#000720"></line>
        <text x="20" y="140">-R</text>
        <line x1="148" y1="30" x2="152" y2="30" stroke="#000720"></line>
        <text x="156" y="35">R</text>
        <line x1="148" y1="90" x2="152" y2="90" stroke="#000720"></line>
        <text x="156" y="95">R/2</text>
        <line x1="148" y1="210" x2="152" y2="210" stroke="#000720"></line>
        <text x="156" y="215">-R/2</text>
        <line x1="148" y1="270" x2="152" y2="270" stroke="#000720"></line>
        <text x="156" y="275">-R</text>

        <polygon points="300,150 295,155 295, 145" fill="#000720" stroke="#000720"></polygon>
        <polygon points="150,0 145,5 155,5" fill="#000720" stroke="#000720"></polygon>

        <!-- Квадрат в верхней правой четверти -->
        <rect x="150" y="30" width="120" height="120" fill-opacity="0.4" stroke="navy" fill="blue"></rect>

        <!-- Треугольник в нижней правой четверти -->
        <polygon points="150,150 270,150 150,210" fill-opacity="0.4" stroke="navy" fill="blue"></polygon>

        <!-- Круг в верхней левой четверти -->
        <path d="M 150 150 L 30 150 A 120 120 0 0 1 150 30 Z" fill-opacity="0.4" stroke="navy" fill="blue"></path>
      </svg>
    </td>
  </tr>

  <tr>
    <td rowspan="9">Выберите Y:</td>
    <td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="-5">-5</td>
  </tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="-4">-4</td></tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="-3">-3</td></tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="-2">-2</td></tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="-1">-1</td></tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="0" checked>0</td></tr>gradle
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="1">1</td></tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="2">2</td></tr>
  <tr><td colspan="3"><input name="Y-radio-group" class="illuminated animated" type="radio" value="3">3</td></tr>

  <tr>
    <td>Введите R:</td>
    <td colspan="3"><input required name="R-input" class="illuminated animated" type="text" placeholder="1...4" maxlength="6"></td>
  </tr>

  <tr>
    <td colspan="5">
      <button type="submit" id="checkButton">Проверить</button>
    </td>
  </tr>

  <tr>
    <td colspan="5">
      <hr>
    </td>
  </tr>
  </tbody>

    <tfoot>
      <tr>
        <td colspan="5" id="outputContainer">
          <%
             List<Point> pointsList = (List<Point>) session.getAttribute("pointsList");
             if (pointsList == null || pointsList.isEmpty()) {
          %>
          <h4>
            <span id="notifications" class="outputStub notification">Нет результатов</span>
          </h4>
          <table id="outputTable">
            <tr>
              <th>X</th>
              <th>Y</th>
              <th>R</th>
              <th>Точка входит в ОДЗ</th>
            </tr>
          </table>
          <% } else { %>
          <h4>
            <span class="notification"></span>
          </h4>
          <table id="outputTable">
            <tr>
              <th>X</th>
              <th>Y</th>
              <th>R</th>
              <th>Точка входит в ОДЗ</th>
            </tr>
            <% for (Point point : pointsList) { %>
            <tr>
              <td>
                <%= point.getX() %>
              </td>
              <td>
                <%= point.getY() %>
              </td>
              <td>
                <%= point.getR() %>
              </td>
              <td>
                <%= point.isInArea() ? "<span class=\"success\">Попал</span>"
                  : "<span class=\"fail\">Промазал</span>" %>
              </td>
            </tr>
            <% } %>
          </table>
          <% } %>
        </td>
      </tr>
    </tfoot>


</table>

<footer class="shaded animated">
  <figure>
    <a href="https://se.ifmo.ru">
      <img class="illuminated" src="images/logo.png"
           alt="Факультет Программной инженерии и компьютерной техники Университета ИТМО"
           title="Перейти на сайт ПИиКТ ИТМО">
    </a>
    <figcaption>2023</figcaption>
  </figure>
</footer>

<script
  src="https://code.jquery.com/jquery-3.7.1.min.js"
  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
  crossorigin="anonymous"></script>
<script src="script.js"></script>
</body>

</html>