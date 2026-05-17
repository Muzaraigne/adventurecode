package org.example.utils;

/**
 * Interface pour les directions (Open/Closed Principle: extensible)
 */
public interface Direction {
    void move(Point point);

    static Direction fromChar(char c) {
        return switch (c) {
            case 'R' -> new RightDirection();
            case 'L' -> new LeftDirection();
            case 'U' -> new UpDirection();
            case 'D' -> new DownDirection();
            default -> throw new IllegalArgumentException("Direction inconnue: " + c);
        };
    }
}

class RightDirection implements Direction {
    @Override
    public void move(Point point) {
        point.moveR();
    }
}

class LeftDirection implements Direction {
    @Override
    public void move(Point point) {
        point.moveL();
    }
}

class UpDirection implements Direction {
    @Override
    public void move(Point point) {
        point.moveU();
    }
}

class DownDirection implements Direction {
    @Override
    public void move(Point point) {
        point.moveD();
    }
}

