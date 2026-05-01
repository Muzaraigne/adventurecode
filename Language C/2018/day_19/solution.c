#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "utilities.h"
#include  "registerOperation.h"

void compute(char* line, int* registers) {
    char name[10];
    int ins[4];
    sscanf(line, "%s %d %d %d", name, &ins[1], &ins[2], &ins[3]);
    if      (strcmp(name, "addr") == 0) addr(registers, ins);
    else if (strcmp(name, "addi") == 0) addi(registers, ins);
    else if (strcmp(name, "mulr") == 0) mulr(registers, ins);
    else if (strcmp(name, "muli") == 0) muli(registers, ins);
    else if (strcmp(name, "banr") == 0) banr(registers, ins);
    else if (strcmp(name, "bani") == 0) bani(registers, ins);
    else if (strcmp(name, "borr") == 0) borr(registers, ins);
    else if (strcmp(name, "bori") == 0) bori(registers, ins);
    else if (strcmp(name, "setr") == 0) setr(registers, ins);
    else if (strcmp(name, "seti") == 0) seti(registers, ins);
    else if (strcmp(name, "gtir") == 0) gtir(registers, ins);
    else if (strcmp(name, "gtri") == 0) gtri(registers, ins);
    else if (strcmp(name, "gtrr") == 0) gtrr(registers, ins);
    else if (strcmp(name, "eqir") == 0) eqir(registers, ins);
    else if (strcmp(name, "eqri") == 0) eqri(registers, ins);
    else if (strcmp(name, "eqrr") == 0) eqrr(registers, ins);
}


int solvePart1( char** instructions, int nblignes) {
    int ip_reg;
    sscanf(instructions[0],"#ip %d",&ip_reg);

    int registers[6] = {0, 0, 0, 0, 0, 0};
    int ip = 0;

    while (ip >= 0 && ip < (nblignes)) {
        registers[ip_reg] = ip;
        compute(instructions[ip+1],registers);
        ip = registers[ip_reg];
        ip++;
    }
    return registers[0];
}
long calculer_somme_diviseurs(int n) {
    long somme = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            somme += i;
        }
    }
    return somme;
}
long solvePart2(char** instructions, int nblignes) {
    int ip_reg;
    sscanf(instructions[0], "#ip %d", &ip_reg);
    int registers[6] = {1, 0, 0, 0, 0, 0};
    int ip = 0;
    int cible = 0;
    for (int i = 0; i < 1000; i++) {
        registers[ip_reg] = ip;
        compute(instructions[ip + 1], registers);
        ip = registers[ip_reg];
        ip++;
        for(int j = 0; j < 6; j++) {
            if (registers[j] > cible) cible = registers[j];
        }
    }


    return calculer_somme_diviseurs(cible);
}

int main(void) {
    int nblignes;
	char** input = extractLines("input.txt",&nblignes);
	if (input == NULL) return EXIT_FAILURE;

    printf("Partie 1: %d\n", solvePart1(input,nblignes));
    printf("Partie 2: %ld\n", solvePart2(input, nblignes));

	free_lines(input);
	return 0;
}
