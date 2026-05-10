package org.example.core;

import org.reflections.Reflections;

import java.util.*;

public class SolutionRegistry {
    private static final String YEARS_PACKAGE = "org.example.years";

    public Map<Integer, List<Day>> discoverSolutions() {
        Reflections reflections = new Reflections(YEARS_PACKAGE);
        Set<Class<? extends Day>> dayClasses = reflections.getSubTypesOf(Day.class);
        Map<Integer, List<Day>> solutions = new TreeMap<>();

        for (Class<? extends Day> dayClass : dayClasses) {
            try {
                Day instance = dayClass.getDeclaredConstructor().newInstance();
                int year = instance.getYear();
                solutions.computeIfAbsent(year, k -> new ArrayList<>()).add(instance);
            } catch (Exception e) {
                System.err.println("Failed to instantiate " + dayClass.getName() + ": " + e.getMessage());
            }
        }

        solutions.values().forEach(list -> list.sort(Comparator.comparingInt(Day::getDay)));
        return solutions;
    }

    public List<Integer> getAvailableYears(Map<Integer, List<Day>> solutions) {
        return new ArrayList<>(solutions.keySet());
    }
}

