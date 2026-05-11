package y2019;

import org.example.years.y2019.Day2;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Day1Test {
    @Test
    void part1() {
        Day1 day = new Day2();
      assertEquals( 30, day.partOne("1,1,1,4,99,5,6,0,99"));
        assertEquals( 3500, day.partOne("1,9,10,3,2,3,11,0,99,30,40,50"));
    }
    @Test
    void part2() {

    }
}
