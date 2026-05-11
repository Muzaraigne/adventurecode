package org.example.years.y2019;

import org.example.core.Day;

public class Day01 implements Day {

    @Override
    public Integer partOne(String input) {
        String[] list = input.split("\n");
        int sum = 0;
        int i = 0;
        while (i < list.length) {
            sum += (Integer.parseInt(list[i])/3)-2;
            i++;
        }
        return sum;
    }

    @Override
    public Integer partTwo(String input) {
        String[] list = input.split("\n");
        int sum = 0;
        int i = 0;
        while (i < list.length) {
            sum += fuelNeeded(Integer.parseInt(list[i]));
            i++;
        }
        return sum;
    }

    @Override
    public int getDay() {
        return 1;
    }

    @Override
    public int getYear() {
        return 2019;
    }

    private int fuelNeeded(int n){
        int next = n/3-2;
        if(next<=0){
            return 0 ;
        }
        else {
            return next + this.fuelNeeded(next);
        }
    }
}
