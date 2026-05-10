package y2019;

import org.example.years.y2019.Day1;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Day1Test {
    @Test
    void part1() {
        Day1 day = new Day1();
        int sol = day.partOne("12");
        assertEquals(2, sol);
        assertEquals(2, day.partOne("14"));
        assertEquals(654, day.partOne("1969"));
        assertEquals( 33583, day.partOne("100756"));
    }
    @Test
    void part2() {
        Day1 day = new Day1();
        assertEquals(2, day.partTwo("14"));
        assertEquals(966, day.partTwo("1969"));
        assertEquals( 50346, day.partTwo("100756"));
    }
}
