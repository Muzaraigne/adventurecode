#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"

int solve_part_1(char** input) {
    int count_twos = 0;
    int count_threes = 0;

    for (int i = 0; input[i] != NULL; i++) {
        int freq[256] = {0};
        // Compter la fréquence de chaque caractère
        for (char* p = input[i]; *p != '\0'; p++) {
            freq[(unsigned char)(*p)]++;
        }

        int has_two = 0;
        int has_three = 0;
        for (int j = 0; j < 256; j++) {
            if (freq[j] == 2) has_two = 1;
            if (freq[j] == 3) has_three = 1;
        }
        count_twos += has_two;
        count_threes += has_three;
    }

    return count_twos * count_threes;
}

char* solve_part_2(char** input) {
    // Allocation dynamique pour le résultat
    char* output = (char*)malloc(256 * sizeof(char));
    if (output == NULL) return NULL;

    for (int i = 0; input[i] != NULL; i++) {
        for (int j = i + 1; input[j] != NULL; j++) {
            int diff_count = 0;
            int len = 0;

            // Calculer la longueur et le nombre de différences
            while (input[i][len] != '\0' && input[j][len] != '\0') {
                if (input[i][len] != input[j][len]) {
                    diff_count++;
                }
                len++;
            }

            // Si exactement une différence, on construit la chaîne commune
            if (diff_count == 1) {
                int out_idx = 0;
                for (int k = 0; k < len; k++) {
                    if (input[i][k] == input[j][k]) {
                        output[out_idx++] = input[i][k];
                    }
                }
                output[out_idx] = '\0'; // Terminateur de chaîne correct
                return output;
            }
        }
    }

    free(output); // Rien trouvé, on libère la mémoire
    return NULL;
}

int main(void) {
    char** input = extractLines("input.txt");
    if (input == NULL) return EXIT_FAILURE;

    char* input_test[] = {
        "abcdef", "bababc", "abbcde", "abcccd",
        "aabcdd", "abcdee", "ababab", NULL
    };

    char* input_test2[] = {
       "abcde", "fghij", "klmno", "pqrst",
       "fguij", "axcye", "wvxyz", NULL
    };

    // --- Part 1 ---
    printf("Part 1 test : %d\n", solve_part_1(input_test));
    printf("Part 1      : %d\n", solve_part_1(input));

    // --- Part 2 ---
    char* res_test2 = solve_part_2(input_test2);
    if (res_test2 != NULL) {
        printf("Part 2 test : %s\n", res_test2);
        free(res_test2); // Important : libérer la mémoire
    }

    char* res_part2 = solve_part_2(input);
    if (res_part2 != NULL) {
        printf("Part 2      : %s\n", res_part2);
        free(res_part2); // Important : libérer la mémoire
    }

    free_lines(input);
    return 0;
}