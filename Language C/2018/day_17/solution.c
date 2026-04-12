#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include "../../utilities.h"

char grid[2000][2000];
int y_min_global = 9999;
int y_max_global = 0;

void scan(char** input) {
    for (int i = 0; input[i]; i++) {
        char co1, co2;
        int min, max, coord;
        sscanf(input[i], "%c=%d, %c=%d..%d", &co1, &coord, &co2, &min, &max);
        if (co1 == 'x') {
            for (int j = min; j <= max; j++) grid[j][coord] = '#';
            if (y_max_global < max) y_max_global = max;
            if (y_min_global > min) y_min_global = min;
        } else {
            for (int j = min; j <= max; j++) grid[coord][j] = '#';
            if (y_max_global < coord) y_max_global = coord;
            if (y_min_global > coord) y_min_global = coord;
        }
    }
}

int is_solid(int y, int x) {
    return grid[y][x] == '#' || grid[y][x] == '~';
}

void flow(int y, int x);


int spread(int y, int x, int *lx_out, int *rx_out) {

    int lx = x;
    int left_closed = 0;
    while (1) {
        if (grid[y][lx - 1] == '#') { left_closed = 1; break; }
        lx--;
        if (!is_solid(y + 1, lx)) break;
        if (grid[y][lx] != '|' && grid[y][lx] != '~') grid[y][lx] = '|';
    }


    int rx = x;
    int right_closed = 0;
    while (1) {
        if (grid[y][rx + 1] == '#') { right_closed = 1; break; }
        rx++;
        if (!is_solid(y + 1, rx)) break;
        if (grid[y][rx] != '|' && grid[y][rx] != '~') grid[y][rx] = '|';
    }

    *lx_out = lx;
    *rx_out = rx;
    return left_closed && right_closed;
}

void flow(int y, int x) {
    if (y > y_max_global) return;
    if (grid[y][x] == '|' || grid[y][x] == '~' || grid[y][x] == '#') return;

    grid[y][x] = '|';


    if (!is_solid(y + 1, x)) {
        flow(y + 1, x);
        if (!is_solid(y + 1, x)) return;
    }


    while (1) {
        int lx, rx;
        int closed = spread(y, x, &lx, &rx);

        if (closed) {

            for (int j = lx; j <= rx; j++) grid[y][j] = '~';
            y--;
            if (y < 1) break;
        } else {

            if (!is_solid(y + 1, lx)) flow(y, lx);
            if (!is_solid(y + 1, rx)) flow(y, rx);
            break;
        }
    }
}

void* run(void* arg) {
    (void)arg;
    flow(1, 500);
    return NULL;
}

int main(void) {
    char** input = extractLines("input.txt", NULL);
    if (input == NULL) return EXIT_FAILURE;

    memset(grid, ' ', sizeof(grid));
    scan(input);
    grid[0][500] = '+';

    pthread_t thread;
    pthread_attr_t attr;
    pthread_attr_init(&attr);
    pthread_attr_setstacksize(&attr, 64 * 1024 * 1024);
    pthread_create(&thread, &attr, run, NULL);
    pthread_join(thread, NULL);
    pthread_attr_destroy(&attr);

    int part1 = 0, part2 = 0;
    for (int y = y_min_global; y <= y_max_global; y++) {
        for (int x = 0; x < 2000; x++) {
            if (grid[y][x] == '|' || grid[y][x] == '~') part1++;
            if (grid[y][x] == '~') part2++;
        }
    }

    printf("Part 1: %d\n", part1);
    printf("Part 2: %d\n", part2);

    free_lines(input);
    return 0;
}