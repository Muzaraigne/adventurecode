package org.example.years.y2019;

import org.example.core.Day;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day04 extends Day {

    // Cette regex valide UNIQUEMENT la longueur (6) et la croissance (0*1*2*...)
    private static final String GROWTH_REGEX = "^(?=\\d{6}$)0*1*2*3*4*5*6*7*8*9*$";
    private static final Pattern GROWTH_PATTERN = Pattern.compile(GROWTH_REGEX);

    // Regex pour découper le nombre en groupes de chiffres identiques (ex : "111", "22")
    private static final Pattern GROUP_PATTERN = Pattern.compile("(\\d)\\1*");

    public Day04() {
        super(4, 2019);
    }

    @Override
    public Object partOne(String input) {
        return countValidPasswords(input, false);
    }

    @Override
    public Object partTwo(String input) {
        return countValidPasswords(input, true);
    }

    /**
     * Méthode générique qui gère la boucle et l'extraction des bornes
     * pour limiter la duplication entre Part 1 et Part 2.
     */
    private int countValidPasswords(String input, boolean isPartTwo) {
        String[] borne = input.trim().split("-");
        int bmin = Integer.parseInt(borne[0]);
        int bmax = Integer.parseInt(borne[1]);

        int count = 0;
        for (int i = bmin; i <= bmax; i++) {
            if (isValidPassword(String.valueOf(i), isPartTwo)) {
                count++;
            }
        }
        return count;
    }

    /**
     * Valide le mot de passe selon les critères de croissance et de doublons.
     */
    private boolean isValidPassword(String passwordStr, boolean isPartTwo) {

        if (!GROWTH_PATTERN.matcher(passwordStr).matches()) {
            return false;
        }

        Matcher matcher = GROUP_PATTERN.matcher(passwordStr);
        boolean hasDouble = false;

        while (matcher.find()) {
            int groupLength = matcher.group().length();

            if (isPartTwo) {
                if (groupLength == 2) {
                    return true;
                }
            } else {
                // Partie 1 : Un groupe de 2 chiffres OU PLUS (>= 2) fonctionne
                if (groupLength >= 2) {
                    hasDouble = true;
                }
            }
        }

        return hasDouble;
    }
}