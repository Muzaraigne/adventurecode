package org.example.years.y2019;

import org.example.core.Day;
import org.example.utils.Direction;
import org.example.utils.Point;

import java.util.HashMap;
import java.util.Map;

/**
 * Jour 3 - Crossed Wires
 * Utilise les principes SOLID :
 * - SRP : méthodes pour chaque responsabilité
 * - OCP : extensible via l'interface Direction
 * - LSP : implémente correctement l'interface Day
 */
public class Day03 extends Day {
    private static final Point ORIGIN = new Point(0, 0);

    public Day03() {
        super(3, 2019);
    }

    @Override
    public Object partOne(String input) {
        String[] lines = input.trim().split("\n");
        Map<Point, Integer> wire1 = decodeWire(lines[0]);
        Map<Point, Integer> wire2 = decodeWire(lines[1]);

        return findIntersections(wire1, wire2).keySet().stream()
                .mapToInt(p -> p.manathanDistance(ORIGIN))
                .min()
                .orElse(Integer.MAX_VALUE);
    }

    @Override
    public Object partTwo(String input) {
        String[] lines = input.trim().split("\n");
        Map<Point, Integer> wire1 = decodeWire(lines[0]);
        Map<Point, Integer> wire2 = decodeWire(lines[1]);

        return findIntersections(wire1, wire2).values().stream()
                .mapToInt(Integer::intValue)
                .min()
                .orElse(Integer.MAX_VALUE);


    }

    /**
     * Décode une commande de fil en positions avec leurs distances.
     * Format: "R8,U5,L5,D3"
     */
    private Map<Point, Integer> decodeWire(String wireCode) {
        Map<Point, Integer> positions = new HashMap<>();
        Point cursor = new Point(0, 0);
        String[] commands = wireCode.split(",");
        int totalSteps = 0;

        for (String command : commands) {
            char dirChar = command.charAt(0);
            int distance = Integer.parseInt(command.substring(1));

            Direction direction = Direction.fromChar(dirChar);

            for (int i = 0; i < distance; i++) {
                Point p = cursor.copy();
                direction.move(p);
                totalSteps++;
                positions.put(p, totalSteps);
                cursor = p;
            }
        }

        return positions;
    }

    /**
     * Trouve les intersections entre deux fils et retourne
     * les positions avec la somme de leurs distances.
     */
    private Map<Point, Integer> findIntersections(Map<Point, Integer> wire1, Map<Point, Integer> wire2) {
        Map<Point, Integer> intersections = new HashMap<>();
        
        for (Point p : wire1.keySet()) {
            if (wire2.containsKey(p)) {
                int combinedSteps = wire1.get(p) + wire2.get(p);
                intersections.put(p, combinedSteps);
            }
        }
        
        return intersections;
    }
}
