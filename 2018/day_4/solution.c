#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utilities.h"

#define MAX_GUARDS 200

typedef struct {
    int id;
    int total_sleep;
    int minutes[60];
} guard;

int comparer(const void *a, const void *b) {
    const char *c1 = *(const char **)a;
    const char *c2 = *(const char **)b;
    return strcmp(c1, c2);
}

int get_guard_index(guard *guards, int *guard_count, int id) {
    for (int i = 0; i < *guard_count; i++) {
        if (guards[i].id == id) return i;
    }
    int idx = *guard_count;
    guards[idx].id = id;
    (*guard_count)++;
    return idx;
}


int process_logs(char **input, guard *guards) {
    int guard_count = 0;
    int current_guard_idx = -1;
    int sleep_start = 0;

    for (int i = 0; input[i] != NULL; i++) {
        char *line = input[i];
        int minute = atoi(&line[15]);

        if (strstr(line, "Guard")) {
            int id;
            char *hash_ptr = strchr(line, '#');
            sscanf(hash_ptr, "#%d", &id);
            current_guard_idx = get_guard_index(guards, &guard_count, id);
        } else if (strstr(line, "falls asleep")) {
            sleep_start = minute;
        } else if (strstr(line, "wakes up")) {
            if (current_guard_idx != -1) {
                for (int m = sleep_start; m < minute; m++) {
                    guards[current_guard_idx].minutes[m]++;
                    guards[current_guard_idx].total_sleep++;
                }
            }
        }
    }
    return guard_count;
}

int solve_part1(guard *guards, int guard_count) {
    int max_sleep = -1;
    int best_guard_idx = -1;

    // 1. Garde qui dort le plus
    for (int i = 0; i < guard_count; i++) {
        if (guards[i].total_sleep > max_sleep) {
            max_sleep = guards[i].total_sleep;
            best_guard_idx = i;
        }
    }

    if (best_guard_idx == -1) return 0;

    // 2. Minute la plus fréquente pour ce garde
    int best_minute = -1;
    int max_freq = -1;
    for (int m = 0; m < 60; m++) {
        if (guards[best_guard_idx].minutes[m] > max_freq) {
            max_freq = guards[best_guard_idx].minutes[m];
            best_minute = m;
        }
    }

    return guards[best_guard_idx].id * best_minute;
}

int solve_part2(guard *guards, int guard_count) {
    int max_freq = -1;
    int result = 0;

    for (int i = 0; i < guard_count; i++) {
        for (int m = 0; m < 60; m++) {
            if (guards[i].minutes[m] > max_freq) {
                max_freq = guards[i].minutes[m];
                result = guards[i].id * m;
            }
        }
    }
    return result;
}

int main(void) {
    char** input = extractLines("input.txt");
    if (input == NULL) return EXIT_FAILURE;

    int size = 0;
    for (int i = 0 ; input[i] != NULL ; i++) size++;
    qsort(input, size, sizeof(char*), comparer);

    guard guards[MAX_GUARDS] = {0};
    int guard_count = process_logs(input, guards);

    printf("Resultat Part 1: %d\n", solve_part1(guards, guard_count));
    printf("Resultat Part 2: %d\n", solve_part2(guards, guard_count));

    free_lines(input);
    return 0;
}
