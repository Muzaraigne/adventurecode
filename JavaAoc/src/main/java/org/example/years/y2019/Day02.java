package org.example.years.y2019;

import java.util.ArrayList;

import org.example.core.Day;


public class Day02 extends Day {
    
    Day02(){
		super(2,2019);
	}
    public Integer partOne(String input) {
      ArrayList<Integer> op = parse(input);
      op.set(1, 12);
      op.set(2, 2);
      cycle(op);
      return op.get(0);
    }

	private ArrayList<Integer> parse(String input) {
		ArrayList<Integer> op= new ArrayList<>();
		  for (String c : input.trim().split(",")) {
			    op.add(Integer.parseInt(c.trim()));
			}
		return op;
	}

	private void cycle(ArrayList<Integer> op) {
		int cursor = 0;
		  while (op.get(cursor) != 99) {
			    int opcode = op.get(cursor);
			    int pos1 = op.get(cursor + 1);
			    int pos2 = op.get(cursor + 2);
			    int pos3 = op.get(cursor + 3);

			    if (opcode == 1) {
			        op.set(pos3, op.get(pos1) + op.get(pos2));
			    } else if (opcode == 2) {
			        op.set(pos3, op.get(pos1) * op.get(pos2));
			    } else {
			        throw new RuntimeException("Opcode inconnu : " + opcode);
			    }

			    cursor += 4;
			}
	}


    public Integer partTwo(String input) {
    	int obj = 19690720;
    	for(int i = 0;i<99;i++) {
    		for(int j=0;j<99;j++) {
    			ArrayList<Integer> op = parse(input);
    			op.set(1, i);
    			op.set(2, j);
    			cycle(op);
    			if(op.get(0) == obj) {
    				return 100 *i + j;
    			}
    		}
    	}
      return 0;
    }




}
