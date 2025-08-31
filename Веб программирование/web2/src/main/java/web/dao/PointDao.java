package web.dao;

import web.models.Point;

import java.io.Serializable;
import java.util.List;
import java.util.ArrayList;

public class PointDao implements Serializable {
    private final List<Point> points = new ArrayList<Point>();

    public void addPoint(Point point) {
        points.add(point);
    }

    public List<Point> getPoints() {
        return points;
    }
}