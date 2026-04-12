#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utilities.h"

int rows, cols;

void strip_cr(char** grid, int r) {
    for (int i = 0; i < r; i++) {
        int len = strlen(grid[i]);
        if (len > 0 && grid[i][len-1] == '\r')
            grid[i][len-1] = '\0';
    }
}

void count_neighbors(char** grid, int y, int x, int* trees, int* lumber, int* open) {
    *trees = *lumber = *open = 0;
    for (int dy = -1; dy <= 1; dy++) {
        for (int dx = -1; dx <= 1; dx++) {
            if (dy == 0 && dx == 0) continue;
            int ny = y + dy, nx = x + dx;
            if (ny < 0 || ny >= rows || nx < 0 || nx >= cols) continue;
            if (grid[ny][nx] == '|') (*trees)++;
            if (grid[ny][nx] == '#') (*lumber)++;
            if (grid[ny][nx] == '.') (*open)++;
        }
    }
}

char** next_gen(char** grid) {
    char** newGrid = malloc(sizeof(char*) * (rows + 1));
    for (int i = 0; i < rows; i++) {
        newGrid[i] = malloc(cols + 1);
        newGrid[i][cols] = '\0';
    }
    newGrid[rows] = NULL;

    for (int y = 0; y < rows; y++) {
        for (int x = 0; x < cols; x++) {
            int trees, lumber, open;
            count_neighbors(grid, y, x, &trees, &lumber, &open);
            char c = grid[y][x];
            if      (c == '.' && trees  >= 3) newGrid[y][x] = '|';
            else if (c == '|' && lumber >= 3) newGrid[y][x] = '#';
            else if (c == '#' && !(lumber >= 1 && trees >= 1)) newGrid[y][x] = '.';
            else                              newGrid[y][x] = c;
        }
    }
    return newGrid;
}

void free_grid(char** grid) {
    for (int i = 0; grid[i] != NULL; i++) free(grid[i]);
    free(grid);
}

int score(char** grid) {
    int trees = 0, lumber = 0;
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++) {
            if (grid[y][x] == '|') trees++;
            if (grid[y][x] == '#') lumber++;
        }
    return trees * lumber;
}

char* serialize(char** grid) {
    char* s = malloc(rows * cols + 1);
    int k = 0;
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++)
            s[k++] = grid[y][x];
    s[k] = '\0';
    return s;
}

void solve(const char* filename, int is_test) {
    char** grid = extractLines(filename, &rows);
    if (grid == NULL) return;
    strip_cr(grid, rows);
    cols = strlen(grid[0]);


    char** current = grid;
    for (int i = 0; i < 10; i++) {
        char** ng = next_gen(current);
        if (current != grid) free_grid(current);
        current = ng;
    }
    printf("%s Part 1: %d\n", is_test ? "Test" : "Real", score(current));
    free_grid(current);

    if (is_test) { free_lines(grid); return; }


    grid = extractLines(filename, &rows);
    strip_cr(grid, rows);
    cols = strlen(grid[0]);

    int   max_states = 10000;
    char** states    = malloc(sizeof(char*) * max_states);
    int   n_states   = 0;
    int   target     = 1000000000;
    current          = grid;
    int   found      = 0;

    for (int t = 0; t < target && !found; t++) {
        char* s = serialize(current);

        for (int k = 0; k < n_states; k++) {
            if (strcmp(states[k], s) == 0) {
                int cycle_len = t - k;
                int remaining = (target - k) % cycle_len;
                free(s);

                char** g = extractLines(filename, &rows);
                strip_cr(g, rows);
                cols = strlen(g[0]);
                for (int i = 0; i < k + remaining; i++) {
                    char** ng = next_gen(g);
                    free_grid(g);
                    g = ng;
                }
                printf("Real Part 2: %d\n", score(g));
                free_grid(g);
                found = 1;
                break;
            }
        }
        if (!found) {
            states[n_states++] = s;
            char** ng = next_gen(current);
            if (current != grid) free_grid(current);
            current = ng;
        }
    }

    for (int i = 0; i < n_states; i++) free(states[i]);
    free(states);
    if (current != grid) free_grid(current);
    free_lines(grid);
}

int main(void) {
    solve("../2018/day_18/test.txt", 1);
    solve("input.txt", 0);
    return 0;
}