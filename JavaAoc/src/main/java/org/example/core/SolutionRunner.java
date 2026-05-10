package org.example.core;

import java.util.ArrayList;
import java.util.List;

public class SolutionRunner {
    private final List<Day> days;
    private final String cookie;
    private final AocClient aocClient = new AocClient();
    private final InputStorage inputStorage  = new InputStorage();

    public SolutionRunner(List<Day> days, String cookie) {
        this.days = days;
        this.cookie = cookie;
    }

    public SolutionRunner(String cookie){
        this.days = new ArrayList<>();
        this.cookie = cookie;
    }

    public void runAll() {
        for (Day day : days) {
            run(day);
        }
    }

    public void run(Day day) {
        int year = day.getYear();
        int dayNum = day.getDay();

        // Try to load input from storage
        String input = inputStorage.load(year, dayNum)
                .orElseGet(() -> {
                    // Fetch from AoC if not found
                    String fetchedInput = aocClient.fetchInput(year, dayNum, cookie);
                    inputStorage.save(year, dayNum, fetchedInput);
                    return fetchedInput;
                });

        // Run both parts
        Object partOneResult = day.partOne(input);
        Object partTwoResult = day.partTwo(input);

        // Display results
        System.out.println("── Day " + dayNum + " " + "─".repeat(Math.max(0, 23 - String.valueOf(dayNum).length())));
        System.out.println("Part 1 : " + partOneResult);
        System.out.println("Part 2 : " + partTwoResult);
        System.out.println();
    }
}



