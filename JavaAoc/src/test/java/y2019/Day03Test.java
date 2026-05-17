package y2019;


import org.example.years.y2019.Day03;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Day03Test {
    @Test
    void part1() {
        Day03 day = new Day03();
        String inputTest =
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
            "U62,R66,U55,R34,D71,R55,D58,R83";
        assertEquals(159, day.partOne(inputTest));
        inputTest =
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n" +
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7";
        assertEquals(135, day.partOne(inputTest));

    }

    @Test
    void part2() {
        Day03 day = new Day03();
        String inputTest =
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\n" +
                "U62,R66,U55,R34,D71,R55,D58,R83";
        assertEquals(610, day.partTwo(inputTest));
        inputTest =
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n" +
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7";
        assertEquals(410, day.partTwo(inputTest));

    }

}
