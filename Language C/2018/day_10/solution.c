#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include "../../utilities.h"

typedef struct {
    long x, y;
    long vx, vy;
} Point;

// Analyse le texte pour extraire les positions et vitesses
Point* parseInput(char** lines, int* count) {
    *count = 0;
    while (lines[*count] != NULL) (*count)++;

    Point* points = malloc(sizeof(Point) * (*count));
    for (int i = 0; i < *count; i++) {
        char* p = lines[i];
        char* end;

        while (*p && *p != '-' && (*p < '0' || *p > '9')) p++;
        points[i].x = strtol(p, &end, 10); p = end;

        while (*p && *p != '-' && (*p < '0' || *p > '9')) p++;
        points[i].y = strtol(p, &end, 10); p = end;

        while (*p && *p != '-' && (*p < '0' || *p > '9')) p++;
        points[i].vx = strtol(p, &end, 10); p = end;

        while (*p && *p != '-' && (*p < '0' || *p > '9')) p++;
        points[i].vy = strtol(p, &end, 10);
    }
    return points;
}

// Calcule les dimensions de la boîte englobante
void getBounds(Point* pts, int n, long* minX, long* maxX, long* minY, long* maxY) {
    *minX = *maxX = pts[0].x;
    *minY = *maxY = pts[0].y;
    for (int i = 1; i < n; i++) {
        if (pts[i].x < *minX) *minX = pts[i].x;
        if (pts[i].x > *maxX) *maxX = pts[i].x;
        if (pts[i].y < *minY) *minY = pts[i].y;
        if (pts[i].y > *maxY) *maxY = pts[i].y;
    }
}

// Affiche les points dans une grille de caractères
void display(Point* pts, int n) {
    long minX, maxX, minY, maxY;
    getBounds(pts, n, &minX, &maxX, &minY, &maxY);

    long width  = maxX - minX + 1;
    long height = maxY - minY + 1;

    // Sécurité pour éviter d'allouer trop de mémoire si ce n'est pas le bon moment
    if (width > 600 || height > 158 || width <= 0 || height <= 0) {
        printf("ERREUR: grille trop large (%ldx%ld). Le message n'est pas encore formé.\n", width, height);
        return;
    }

    char* grid = calloc((size_t)(width * height), 1);
    if (!grid) return;

    for (int i = 0; i < n; i++) {
        int gx = (int)(pts[i].x - minX);
        int gy = (int)(pts[i].y - minY);
        grid[gy * width + gx] = 1;
    }

    for (long y = 0; y < height; y++) {
        for (long x = 0; x < width; x++)
            putchar(grid[y * width + x] ? '#' : '.');
        putchar('\n');
    }
    free(grid);
}

// Déplace les points selon la direction (1 pour avancer, -1 pour reculer)
void step(Point* pts, int n, int seconds) {
    for (int i = 0; i < n; i++) {
        pts[i].x += (long)seconds * pts[i].vx;
        pts[i].y += (long)seconds * pts[i].vy;
    }
}

// Trouve le moment où la hauteur de la boîte englobante est minimale
int findMinTime(Point* pts, int n) {
    long minX, maxX, minY, maxY;
    long prevHeight;
    int t = 0;

    getBounds(pts, n, &minX, &maxX, &minY, &maxY);
    prevHeight = maxY - minY;

    // Phase 1 : Avance rapide par pas de 100
    while (1) {
        step(pts, n, 100);
        getBounds(pts, n, &minX, &maxX, &minY, &maxY);
        long height = maxY - minY;

        if (height > prevHeight) {
            step(pts, n, -100); // Trop loin, on revient au dernier état stable
            break;
        }
        t += 100;
        prevHeight = height;
    }

    // Phase 2 : Affinage pas à pas (1 seconde)
    while (1) {
        step(pts, n, 1);
        getBounds(pts, n, &minX, &maxX, &minY, &maxY);
        long height = maxY - minY;

        if (height > prevHeight) {
            step(pts, n, -1); // On revient à la seconde précise du minimum
            break;
        }
        t++;
        prevHeight = height;
    }

    return t;
}

int main(void) {
    // --- DONNÉES DE TEST ---
    char* test_lines[] = {
        "position=< 9,  1> velocity=< 0,  2>", "position=< 7,  0> velocity=<-1,  0>",
        "position=< 3, -2> velocity=<-1,  1>", "position=< 6, 10> velocity=<-2, -1>",
        "position=< 2, -4> velocity=< 2,  2>", "position=<-6, 10> velocity=< 2, -2>",
        "position=< 1,  8> velocity=< 1, -1>", "position=< 1,  7> velocity=< 1,  0>",
        "position=<-3, 11> velocity=< 1, -2>", "position=< 7,  6> velocity=<-1, -1>",
        "position=<-2,  3> velocity=< 1,  0>", "position=<-4,  3> velocity=< 2,  0>",
        "position=<10, -3> velocity=<-1,  1>", "position=< 5, 11> velocity=< 1, -2>",
        "position=< 4,  7> velocity=< 0, -1>", "position=< 8, -2> velocity=< 0,  1>",
        "position=<15,  0> velocity=<-2,  0>", "position=< 1,  6> velocity=< 1,  0>",
        "position=< 8,  9> velocity=< 0, -1>", "position=< 3,  3> velocity=<-1,  1>",
        "position=< 0,  5> velocity=< 0, -1>", "position=<-2,  2> velocity=< 2,  0>",
        "position=< 5, -2> velocity=< 1,  2>", "position=< 1,  4> velocity=< 2,  1>",
        "position=<-2,  7> velocity=< 2, -2>", "position=< 3,  6> velocity=<-1, -1>",
        "position=< 5,  0> velocity=< 1,  0>", "position=<-6,  0> velocity=< 2,  0>",
        "position=< 5,  9> velocity=< 1, -2>", "position=<14,  7> velocity=<-2,  0>",
        "position=<-3,  6> velocity=< 2, -1>", NULL
    };

    int n_test;
    Point* pts_test = parseInput(test_lines, &n_test);
    int t_test = findMinTime(pts_test, n_test);
    printf("=== Test (après %d secondes) ===\n", t_test);
    display(pts_test, n_test);
    free(pts_test);

    // --- PARTIE RÉELLE ---
    char** input = extractLines("input.txt", NULL);
    if (!input) {
        printf("Erreur : Impossible de lire input.txt\n");
        return EXIT_FAILURE;
    }

    int n;
    Point* pts = parseInput(input, &n);
    int t = findMinTime(pts, n);

    printf("\n=== Partie 1 (Message) ===\n");
    display(pts, n);
    printf("\n=== Partie 2 (Temps écoulé) ===\n");
    printf("Le message est apparu après %d secondes.\n", t);

    free(pts);
    free_lines(input);
    return 0;
}