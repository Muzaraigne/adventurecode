#include <stdio.h>
    #include <stdlib.h>
    #include <limits.h>
    #include "../../utilities.h"

    typedef struct {
        int x;
        int y;
    } point;

    typedef struct {
        int size;
        int infinite;
        point coords;
    } area;

    int distance(point a, point b) {
        return abs(a.x - b.x) + abs(a.y - b.y);
    }

    point convert_data(char** lines, area* tab) {
        int max_x = 0;
        int max_y = 0;
        for (int i = 0; lines[i] != NULL; i++) {
            sscanf(lines[i], "%d, %d", &tab[i].coords.x, &tab[i].coords.y);

            tab[i].size = 0;
            tab[i].infinite = 0;

            if (tab[i].coords.x > max_x) max_x = tab[i].coords.x;
            if (tab[i].coords.y > max_y) max_y = tab[i].coords.y;
        }
        point pointMax = {max_x, max_y};
        return pointMax;
    }

    void calculate(area* tab, point pointMax, int size) {
        for (int x = 0; x <= pointMax.x; x++) {
            for (int y = 0; y <= pointMax.y; y++) {
                point currentPoint = {x, y};
                int minDist = INT_MAX;
                int minInd = -1;
                int tie = 0;

                for (int i = 0; i < size; i++) {
                    int dist = distance(tab[i].coords, currentPoint);
                    if (dist < minDist) {
                        minDist = dist;
                        minInd = i;
                        tie = 0;
                    } else if (dist == minDist) {
                        tie = 1;
                    }
                }

                if (!tie && minInd != -1) {
                    tab[minInd].size++;
                    if (x == 0 || x == pointMax.x || y == 0 || y == pointMax.y) {
                        tab[minInd].infinite = 1;
                    }
                }
            }
        }
    }

    int solve_part1(char** line, int size, area* tab,point pointMax) {
        int max_area = 0;

        if (tab == NULL) return -1;

        calculate(tab, pointMax, size);

        for (int i = 0; i < size; i++) {
            if (!tab[i].infinite && tab[i].size > max_area) {
                max_area = tab[i].size;
            }
        }
        return max_area;
    }

    int solve_part2(int size, area* tab,point maxPoint) {
        int safeAreaSize = 0;
        int limit = 10000;
        int max_x = maxPoint.x;
        int max_y = maxPoint.y;
        for (int x = 0; x <= max_x; x++) {
            for (int y = 0; y <= max_y; y++) {
                int totalDist = 0;
                point currentPoint = {x, y};
                for (int i = 0; i < size; i++) {
                    totalDist += distance(currentPoint, tab[i].coords);
                }
                if (totalDist < limit) {
                    safeAreaSize++;
                }
            }
        }
        return safeAreaSize;
    }

    int main(void) {
        int size = 0;
        char** input = extractLines("input.txt", &size);
        if (input == NULL ){
            fprintf(stderr, "Erreur de lecture du fichier\n");
            return EXIT_FAILURE;
        }

        area* tab = malloc(sizeof(area) * size);
        point maxPoint = convert_data(input, tab);
        if (tab == NULL) return EXIT_FAILURE;
        int result1 = solve_part1(input, size, tab,maxPoint);
        printf("Resultat Part 1: %d\n", result1);
        int result2 = solve_part2(size, tab,maxPoint);
        printf("Resultat Part 2: %d\n", result2);

        free(tab);
        free_lines(input);
        return 0;
    }