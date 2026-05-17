package org.example.utils;

import java.util.Objects;

public class Point {
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public boolean equals(Object obj) {
        if (obj instanceof Point p) {
            return p.x == this.x && p.y == this.y;
        }
        else  {
            return false;
        }
    }
    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
    public int manathanDistance(Point target) {
        return Math.abs(this.x - target.x) + Math.abs(this.y - target.y);
    }

    public void moveR(){
        this.x = this.x + 1;
    }
    public void moveL(){
        this.x = this.x - 1;
    }
    public void moveU(){
        this.y = this.y + 1;
    }
    public void moveD(){
        this.y = this.y - 1;
    }

    public Point copy(){
        return new Point(this.x, this.y);
    }
}
