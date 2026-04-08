#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"


int calculatePowerLevel(int x, int y , int serialNumber) {
    int rackId = x + 10;
    int power = rackId * y;
    power += serialNumber;
    power *= rackId;
    int hundreds = (power / 100) % 10;
    return hundreds - 5;
}

int squarePowerLevel(int centerX, int centerY, int serialNumber,int size) {
    int totalPower = 0;
    for (int y = centerY; y < centerY + size; y++) {
        for (int x = centerX; x < centerX +size ; x++) {
            totalPower += calculatePowerLevel(x, y, serialNumber);
        }
    }
    return totalPower;
}

char* solvePart1(int maxX, int maxY,int serialNumber) {
    char *s = malloc(16 * sizeof(char));
    if (s == NULL) return NULL;
    int maxPower = INT_MIN;
    int bestX = 0;
    int bestY = 0;

    for (int y = 1; y <= maxY - 2; y++) {
        for (int x = 1; x <= maxX - 2; x++) {
            int currentPower = squarePowerLevel(x, y, serialNumber,3);
            if (currentPower > maxPower) {
                maxPower = currentPower;
                bestX = x;
                bestY = y;
            }
        }
    }
    sprintf(s, "%d,%d", bestX, bestY);
    return s;
}

char* solvePart2(int maxX, int maxY,int serialNumber) {
    char *s = malloc(32 * sizeof(char));
    if (s == NULL) return NULL;

    int table[301][301] = {0};
    for (int y = 1; y <= maxY; y++) {
        for (int x = 1; x <= maxX; x++) {
            int p = calculatePowerLevel(x, y, serialNumber);
            table[y][x] = p + table[y-1][x] + table[y][x-1] - table[y-1][x-1];
        }
    }

    int maxPower = INT_MIN;
    int bestX = 0;
    int bestY = 0;
    int bestSize = 0;

    for (int size = 1; size <= 300; size++) {
        for (int y = 1; y <= maxY - size + 1; y++) {
            for (int x = 1; x <= maxX - size + 1; x++) {
                int x2 = x + size - 1;
                int y2 = y + size - 1;
                int currentPower = table[y2][x2] - table[y-1][x2] - table[y2][x-1] + table[y-1][x-1];

                if (currentPower > maxPower) {
                    maxPower = currentPower;
                    bestX = x;
                    bestY = y;
                    bestSize = size;
                }
            }
        }
    }

    sprintf(s, "%d,%d,%d", bestX, bestY, bestSize);
    return s;
}

int main(void) {
    int inputTest = 18;
    char* result = solvePart1(300, 300, inputTest);
    char* result2 = solvePart2(300, 300, inputTest);
    printf("Test Value (18): %s\n", result); // Expected: 33,45
    printf("Test Part 2 Value(18):%s \n",result2);// Expected :90,269,16
    free(result);
    free(result2);

    int inputReal = 6303;
    char* resultReal = solvePart1(300, 300, inputReal);
    char* resultReal2 = solvePart2(300, 300, inputReal);
    printf("Real Result To Part 1: %s\n", resultReal);
    printf("Real Result To Part 2:%s \n",result2);

    free(resultReal);
    free(resultReal2);

    return 0;
}