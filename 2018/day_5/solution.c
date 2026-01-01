#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "../../utilities.h"

char* simplification(const char* line, const int length) {
    char* stack = malloc((length + 1) * sizeof(char));
    if (stack == NULL) return NULL;
    int top = -1;

    for (int i = 0; i < length; i++) {
        char current = line[i];
        if (top >= 0 && abs(stack[top] - current) == 32) {
            top--;
        } else {
            stack[++top] = current;
        }
    }
    stack[top + 1] = '\0';
    return stack;
}

int solve_part1(char* line) {
    int length = (int)strlen(line);
    char* reduced = simplification(line, length);

    if (reduced == NULL) return -1;

    int result = (int)strlen(reduced);

    free(reduced);
    return result;
}

int solve_part2(const char* line) {
    const int original_len = (int)strlen(line);
    int min_length = original_len;


    for (int unit = 'a'; unit <= 'z'; unit++) {

        char* filtered = malloc((original_len + 1) * sizeof(char));
        int k = 0;
        for (int i = 0; i < original_len; i++) {
            if (tolower(line[i]) != unit) {
                filtered[k++] = line[i];
            }
        }
        filtered[k] = '\0';
        char* reacted = simplification(filtered, k);
        const int reacted_len = (int)strlen(reacted);

        if (reacted_len < min_length) {
            min_length = reacted_len;
        }
        free(filtered);
        free(reacted);
    }

    return min_length;
}
int main(void) {
	char** input = extractLines("input.txt",NULL);
	if (input == NULL) return EXIT_FAILURE;
    const char * line = input[0];
    char* input_test = "dabAcCaCBAcCcaDA";
    printf("Test Part 1 : %d\n",solve_part1(input_test));
    printf("Part 1 : %d\n", solve_part1(line));
    printf("Part1 : %d\n", solve_part2(line));
	// Ton code ici

	free_lines(input);
	return 0;
}
