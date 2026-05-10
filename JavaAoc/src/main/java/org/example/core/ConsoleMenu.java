package org.example.core;

import java.util.List;
import java.util.Scanner;

public class ConsoleMenu {
    private final Scanner scanner = new Scanner(System.in);

    public int chooseYear(List<Integer> availableYears) {
        while (true) {
            System.out.println("\nAvailable years:");
            for (int i = 0; i < availableYears.size(); i++) {
                System.out.println((i + 1) + ". " + availableYears.get(i));
            }

            System.out.print("Select a year (enter number): ");
            try {
                String input = scanner.nextLine().trim();
                int choice = Integer.parseInt(input);

                if (choice < 1 || choice > availableYears.size()) {
                    System.out.println("Invalid choice. Please enter a number between 1 and " + availableYears.size());
                    continue;
                }

                return availableYears.get(choice - 1);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }
    }
}

