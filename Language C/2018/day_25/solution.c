#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../../utilities.h"

typedef struct {
    int x, y, z, w;
} Point;


int dist_manhattan(Point a, Point b) {
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z) + abs(a.w - b.w);
}


void explorer(int index, int nb_points, Point* pts, int* visite) {
    visite[index] = 1;
    for (int i = 0; i < nb_points; i++) {
        if (!visite[i] && dist_manhattan(pts[index], pts[i]) <= 3) {
            explorer(i, nb_points, pts, visite);
        }
    }
}

int main(void) {
    int nb_lignes = 0;
    char** input = extractLines("input.txt", &nb_lignes);
    if (input == NULL) return EXIT_FAILURE;
    Point* pts = malloc(sizeof(Point) * nb_lignes);
    for (int i = 0; i < nb_lignes; i++) {
        sscanf(input[i], "%d,%d,%d,%d", &pts[i].x, &pts[i].y, &pts[i].z, &pts[i].w);
    }

    int* visite = calloc(nb_lignes, sizeof(int)); // calloc met tout à 0
    int constellations = 0;


    for (int i = 0; i < nb_lignes; i++) {
        if (!visite[i]) {
            constellations++;
            explorer(i, nb_lignes, pts, visite);
        }
    }
    printf("Nombre de constellations : %d\n", constellations);


    free(pts);
    free(visite);
    free_lines(input);
    return 0;
}