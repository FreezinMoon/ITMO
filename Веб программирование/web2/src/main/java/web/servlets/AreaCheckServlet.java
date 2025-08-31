package web.servlets;

import com.google.gson.Gson;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;
import web.models.Point;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@WebServlet("/checkArea")
public class AreaCheckServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    private void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        try {
            double x = Double.parseDouble(request.getParameter("X"));
            int y = Integer.parseInt(request.getParameter("Y"));
            double r = Double.parseDouble(request.getParameter("R"));
            Point point = new Point(x, y, r);

            // Получаем или создаем список точек в сессии
            HttpSession session = request.getSession();
            List<Point> points = (List<Point>) session.getAttribute("pointsList");
            if (points == null) {
                points = new ArrayList<>();
                session.setAttribute("pointsList", points);
            }

            // Добавляем новую точку в список
            points.add(point);

            String action = request.getParameter("action");
            if ("submitForm".equals(action)) {
                request.setAttribute("X", x);
                request.setAttribute("Y", y);
                request.setAttribute("R", r);
                request.setAttribute("result", point.isInArea());

                jakarta.servlet.RequestDispatcher dispatcher = request.getRequestDispatcher("./result.jsp");
                dispatcher.forward(request, response);
            } else if ("checkPoint".equals(action)) {
                Gson gson = new Gson();
                Map<String, Object> json = new HashMap<>();
                json.put("x", x);
                json.put("y", y);
                json.put("r", r);
                json.put("result", point.isInArea());
                String msg = gson.toJson(json);

                response.setContentType("application/json");
                response.getWriter().write(msg);
            }
        } catch (Exception e) {
            request.getRequestDispatcher("./index.jsp").forward(request, response);
        }
    }
}
