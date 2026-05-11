package y2019;

import org.example.years.y2019.Day02;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class Day02Test {
    @Test
    void part1() {
        Day02 day = new Day02();
        assertEquals( 30, day.partOne("1,1,1,4,99,5,6,0,99"));
        assertEquals( 3500, day.partOne("1,9,10,3,2,3,11,0,99,30,40,50"));
    }
}
