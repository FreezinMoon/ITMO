package web.servlets;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

import com.google.gson.Gson;

import java.io.IOException;
import java.util.HashMap;

@WebServlet("/controller")
public class ControllerServlet extends HttpServlet {
    private static final String INVALID_DATA_MSG = "Please set the data values in correct form.";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        processRequest(request, response);
    }

    private void processRequest(HttpServletRequest request, HttpServletResponse response) throws IOException {
        try {
            String xValue = request.getParameter("X");
            String yValue = request.getParameter("Y");
            String rValue = request.getParameter("R");

            if (isNullOrEmpty(xValue) || isNullOrEmpty(yValue) || isNullOrEmpty(rValue)) {
                sendError(response, INVALID_DATA_MSG);
                return;
            }

            double x = Double.parseDouble(xValue);
            Double.parseDouble(yValue);
            double r = Double.parseDouble(rValue);
            if (x < -5 || x > 3 || r < 1 || r > 4) {
                sendError(response, INVALID_DATA_MSG);
                return;
            }

            response.sendRedirect("./checkArea?" + request.getQueryString());
        } catch (NumberFormatException e) {
            sendError(response, INVALID_DATA_MSG);
        } catch (Exception e) {
            sendError(response, "An error occurred processing your request.");
        }
    }

    private boolean isNullOrEmpty(String str) {
        return str == null || str.isEmpty();
    }

    private void sendError(HttpServletResponse response, final String errorMessage) throws IOException {
        Gson json = new Gson();
        HashMap<String, String> jsonResponse = new HashMap<String, String>() {{
            put("error", errorMessage);
            put("status", "UNPROCESSABLE_ENTITY");
        }};

        response.setContentType("application/json");
        response.getWriter().write(json.toJson(jsonResponse));
        response.setStatus(422);
    }
}
