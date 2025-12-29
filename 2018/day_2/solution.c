#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"


int solve_part_1(char** input) {
    int count_twos = 0;
    int count_threes = 0;
    for (int i =0; input[i] != NULL; i++) {
        int freq[256] = {0};
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
    int checksum = count_twos * count_threes;

    return checksum;
}

char* solve_part_2(char** input) {
    char* output = (char*)malloc(256 * sizeof(char));
    for (int i = 0; input[i] != NULL; i++) {
        for (int j = i + 1; input[j] != NULL; j++) {
            int diff_count = 0;
            int len = 0;
            while (input[i][len] != '\0' && input[j][len] != '\0') {
                if (input[i][len] != input[j][len]) {
                    diff_count++;
                }
                len++;
            }
            if (diff_count == 1) {
                int k;
                int out_idx = 0;
                for (k = 0; k < len; k++) {
                    if (input[i][k] == input[j][k]) {
                        output[out_idx++] = input[i][k];
                    }
                }
                output[out_idx] = '\0'; // Correction ici : guillemets simples
                return output;
            }
        }
    }
    free(output);
    return NULL;
}

int main(void) {
	char** input = extractLines("input.txt");
	if (input == NULL) return EXIT_FAILURE;

	// Ton code ici
    char*input_test[] ={
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
        NULL
    };

    char*input_test2[] ={
       "abcde",
       "fghij",
       "klmno",
       "pqrst",
       "fguij",
       "axcye",
       "wvxyz",
       NULL
    };

    printf("Part 1:  test :%d\n", solve_part_1(input_test));
    printf("Part1 : %d\n", solve_part_1(input));
    printf("Part 2:  test :%d\n", solve_part_2(input_test2));
    printf("Part2 : %s\n", solve_part_2(input));
	free_lines(input);
	return 0;
}
