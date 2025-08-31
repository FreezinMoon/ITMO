package web.models;

public class Point {
    private final double x;
    private final int y;
    private final double r;

    private final boolean isInArea;

    public Point(double x, int y, double r) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.isInArea = isInside(x, y, r);
    }

    private boolean isInside(double x, double y, double r) {
        // Top-right quadrant
        if (x >= 0 && y >= 0) {
            return (x <= r) && (y <= r);
        }
        // Top-left quadrant
        if (x < 0 && y >= 0) {
            return (x * x + y * y) <= (r * r);
        }
        // Bottom-right quadrant
        if (x >= 0 && y < 0) {
            return (y >= (x - r) / 2);
        }

        // Bottom-left quadrant
        return false;
    }

    public double getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public double getR() {
        return r;
    }

    public boolean isInArea() {
        return isInArea;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x && Double.compare(y, point.y) == 0 && r == point.r;
    }

    @Override
    public int hashCode() {
        int result;
        long temp;
        temp = Double.doubleToLongBits(x);
        result = (int) (temp ^ (temp >>> 32));
        result = 31 * result + y;
        temp = Double.doubleToLongBits(r);
        result = 31 * result + (int) (temp ^ (temp >>> 32));
        result = 31 * result + (isInArea ? 1 : 0);
        return result;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                ", r=" + r +
                ", isInArea=" + isInArea +
                '}';
    }
}