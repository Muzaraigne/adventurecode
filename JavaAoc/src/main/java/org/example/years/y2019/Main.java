package org.example.years.y2019;

import org.example.core.SolutionRunner;

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


        SolutionRunner runner = new SolutionRunner(cookie);
        runner.run(new Day02());
    }
}
