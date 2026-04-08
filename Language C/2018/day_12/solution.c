#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"
#include <string.h>

#define BUFFER_SIZE 2000
#define OFFSET 500

char transition_rules[32];
char current_gen[BUFFER_SIZE];
char next_gen[BUFFER_SIZE];

int convertFive(char* s) {
    int result = 0;
    for (int i = 0; i < 5; i++) {
        result <<= 1;
        if (s[i] == '#') {
            result |= 1;
        }
    }
    return result;
}

void parseAndSaveRules(char** inputLines) {
    memset(current_gen, '.', BUFFER_SIZE);
    memset(next_gen, '.', BUFFER_SIZE);

    char* start_ptr = strchr(inputLines[0], ':');
    if (start_ptr) {
        start_ptr += 2;
        memcpy(&current_gen[OFFSET], start_ptr, strlen(start_ptr));
    }

    for (int i = 2; inputLines[i] != NULL; i++) {
        char pattern[6];
        char res;
        if (sscanf(inputLines[i], "%5s => %c", pattern, &res) == 2) {
            int index = convertFive(pattern);
            transition_rules[index] = res;
        }
    }
}


void generation() {
    for (int i = 2; i < BUFFER_SIZE - 2; i++) {
        int index = convertFive(&current_gen[i - 2]);
        next_gen[i] = transition_rules[index];
    }
    memcpy(current_gen, next_gen, BUFFER_SIZE);
    memset(next_gen, '.', BUFFER_SIZE);
}

long long generationScore() {
    long long score = 0;
    for (int i = 0; i < BUFFER_SIZE; i++) {
        if (current_gen[i] == '#') {
            score += (i - OFFSET);
        }
    }
    return score;
}

void resolvePart2() {
    long long lastScore = 0;
    long long lastDiff = 0;
    int stableCount = 0;
    long long targetGen = 50000000000LL;

    for (long long gen = 1; gen <= 1000; gen++) {
        generation();
        long long currentScore = generationScore();
        long long diff = currentScore - lastScore;

        if (diff == lastDiff) {
            stableCount++;
        } else {
            stableCount = 0;
        }
        if (stableCount == 100) {
            long long remainingGens = targetGen - gen;
            long long finalResult = currentScore + (remainingGens * diff);

            printf("Stabilisation détectée à la génération %lld\n", gen);
            printf("Resultat de la partie 2 : %lld\n", finalResult);
            return;
        }

        lastScore = currentScore;
        lastDiff = diff;
    }
}
void resolvePart1(){
    for (int gen=0; gen<20; gen++) {
        generation();
    }
    printf("Resultat de la partie 1 : %lld \n", generationScore());
}


int main(void) {

    memset(transition_rules, '.', 32);


    char** input = extractLines("input.txt", NULL);
    parseAndSaveRules(input);
    resolvePart1();

    parseAndSaveRules(input);
    resolvePart2();

    return 0;
}