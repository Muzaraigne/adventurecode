package org.example.core;

public abstract class Day {
    int nday;
    int year;

    protected Day(int nday, int year){
        this.nday = nday;
        this.year = year;
    }
    public abstract Object partOne(String input);
    public abstract Object partTwo(String input);

    int getDay(){
        return nday;
    }
    int getYear(){
        return year;
    }
}

