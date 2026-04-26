#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utilities.h"
#include "../enigmeUtilities/registerOperation.h"

OpFunc ops[16] = {
    addr, addi, mulr, muli,
    banr, bani, borr, bori,
    setr, seti, gtir, gtri,
    gtrr, eqir, eqri, eqrr
};

int count_valid(int* before, int* instruction, int* after) {
    int count = 0;
    for (int op = 0; op < 16; op++) {
        int regs[4];
        memcpy(regs, before, sizeof(int) * 4);
        ops[op](regs, instruction);
        if (memcmp(regs, after, sizeof(int) * 4) == 0)
            count++;
    }
    return count;
}
void process(char** input) {
    int part1 = 0;
    int i = 0;


    int possible[16];
    for (int k = 0; k < 16; k++) possible[k] = 0xFFFF; // tous candidats au départ

    while (input[i] != NULL && input[i][0] == 'B') {
        int before[4], after[4], instruction[4];

        sscanf(input[i],   "Before: [%d, %d, %d, %d]",
               &before[0], &before[1], &before[2], &before[3]);
        sscanf(input[i+1], "%d %d %d %d",
               &instruction[0], &instruction[1], &instruction[2], &instruction[3]);
        sscanf(input[i+2], "After:  [%d, %d, %d, %d]",
               &after[0], &after[1], &after[2], &after[3]);

        int count = 0;
        int compatible_mask = 0;
        for (int op = 0; op < 16; op++) {
            int regs[4];
            memcpy(regs, before, sizeof(int) * 4);
            ops[op](regs, instruction);
            if (memcmp(regs, after, sizeof(int) * 4) == 0) {
                count++;
                compatible_mask |= (1 << op);
            }
        }

        possible[instruction[0]] &= compatible_mask;

        if (count >= 3) part1++;
        i += 4;
    }

    printf("Part 1: %d\n", part1);


    OpFunc certified[16] = {NULL};
    int resolved = 0;
    while (resolved < 16) {
        for (int k = 0; k < 16; k++) {
            if (certified[k] != NULL) continue;
            if ((possible[k] & (possible[k] - 1)) == 0) {
                int bit = __builtin_ctz(possible[k]);
                certified[k] = ops[bit];
                resolved++;
                for (int j = 0; j < 16; j++)
                    if (j != k) possible[j] &= ~(1 << bit);
            }
        }
    }


    i += 2;
    int r[4] = {0, 0, 0, 0};
    while (input[i] != NULL) {
        int instruction[4];
        sscanf(input[i], "%d %d %d %d",
               &instruction[0], &instruction[1], &instruction[2], &instruction[3]);
        certified[instruction[0]](r, instruction);
        i++;
    }
    printf("Part 2: %d\n", r[0]);
}

int main(void) {
    char** input = extractLines("input.txt", NULL);
    if (input == NULL) return EXIT_FAILURE;

    process(input);

    free_lines(input);
    return 0;
}