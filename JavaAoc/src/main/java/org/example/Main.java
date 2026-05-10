package org.example;

import org.example.core.*;

import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Read AOC_SESSION environment variable
        String cookie = System.getenv("AOC_SESSION");
        if (cookie == null || cookie.isEmpty()) {
            System.err.println("Error: AOC_SESSION environment variable not set.");
            System.err.println("Please set your Advent of Code session cookie:");
            System.err.println("  set AOC_SESSION=your_session_cookie");
            System.exit(1);
        }

        // Discover all solutions
        SolutionRegistry registry = new SolutionRegistry();
        Map<Integer, List<Day>> solutions = registry.discoverSolutions();

        if (solutions.isEmpty()) {
            System.err.println("Error: No solutions found.");
            System.exit(1);
        }

        // Show menu and get year choice
        ConsoleMenu menu = new ConsoleMenu();
        List<Integer> availableYears = registry.getAvailableYears(solutions);
        int chosenYear = menu.chooseYear(availableYears);

        // Run solutions for chosen year
        List<Day> daysForYear = solutions.get(chosenYear);
        SolutionRunner runner = new SolutionRunner(daysForYear, cookie);
        runner.runAll();
    }
}