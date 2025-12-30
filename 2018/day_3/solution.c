#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"

typedef struct {
    int x;
    int y;
    int width;
    int height;
    int id;
} chimney_t;

typedef struct {
    int part1;
    int part2;
} result;

void convert_input(const char* line, chimney_t* chimney) {
    if (sscanf(line, "#%d @ %d,%d: %dx%d", &chimney->id, &chimney->x, &chimney->y, &chimney->width, &chimney->height) != 5) {
        fprintf(stderr, "Erreur de formatage de la ligne : %s\n", line);
    };
}

void solve(char** lines, result* result) {
    int *grid = calloc(1000 * 1000, sizeof(int));
    int overlap_count = 0;
    for (int i = 0 ; lines[i] != NULL ; i++) {
        chimney_t chimney;
        convert_input(lines[i], &chimney);

        for (int dy = 0; dy < chimney.height; dy++) {
            for (int dx = 0; dx < chimney.width; dx++) {
                int index = (chimney.y + dy) * 1000 + (chimney.x + dx);
                if (grid[index] == 1) {
                    overlap_count++;
                }
                grid[index]++;
            }
        }
    }
    result->part1 = overlap_count;

    for (int i = 0 ; lines[i] != NULL ; i++) {
        chimney_t chimney;
        convert_input(lines[i], &chimney);

        int is_intact = 1;

        for (int dy = 0; dy < chimney.height; dy++) {
            for (int dx = 0; dx < chimney.width; dx++) {
                int index = (chimney.y + dy) * 1000 + (chimney.x + dx);
                if (grid[index] > 1) {
                    is_intact = 0;
                    break;
                }
            }
            if (!is_intact) break;
        }

        if (is_intact) {
            result->part2 = chimney.id;
            break;
        }
    }

    free(grid);
}

int main(void) {
    char** input = extractLines("input.txt");
    if (input == NULL) return EXIT_FAILURE;
    result res = {0};

    solve(input, &res);

    printf("Part1 : %d\n", res.part1);
    printf("Part2 : %d\n", res.part2);

    free_lines(input);
    return 0;
}