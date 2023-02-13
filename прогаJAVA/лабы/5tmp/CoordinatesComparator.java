package org.example;

import java.util.Comparator;
import java.util.Objects;

public class CoordinatesComparator implements Comparator<Coordinates> {

    @Override
    public int compare(Coordinates c1, Coordinates c2) {
        if (c1.getX() == c2.getX()) {
            if (Objects.equals(c1.getY(), c2.getY())) return 0;
            if (c1.getY() > c2.getY()) return -1;
            else return 1;
        }
        if (c1.getX() > c2.getY()) return -1;
        else return 1;
    }
}