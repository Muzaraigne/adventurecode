package org.example.years.y2019;

import org.example.core.Day;

public class Day02 implements Day {
    
    @Override
    public Integer partOne(String input) {
      List<Integer> op= new ArrayList();
      for(String c : input.split(",");){
        op.add(Integer.parseInt(c);
      }
      int cursor = 0;
      while(cursor != 99){
        if(op[cursor] == 1){
          op[cursor+3] = op[cursor+1] + op[cursor+2];
        }
        else if (op[cursor] == 2){
          op[cursor+3] = op[cursor+1] * op[cursor+2];
        }
        cursor +=4;
      }
      return 0;
    }

    @Override
    public Integer partTwo(String input) {
      return 0;
    }

    @Override
    public int getDay() {
        return 2;
    }

    @Override
    public int getYear() {
        return 2019;
    }


}
