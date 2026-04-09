#include <stdio.h>
#include <stdlib.h>

void solvepart1(int input) {
    int capacity = input + 20;
    int* result = malloc(sizeof(int) * capacity);
    result[0] = 3;
    result[1] = 7;
    int size = 2;
    int elf1 = 0;
    int elf2 = 1;

    while (size < input + 10) {
        int grade = result[elf1] + result[elf2];
        if (grade >= 10) {
            if (size + 1 >= capacity) {
                capacity *= 2;
                result = realloc(result, sizeof(int) * capacity);
            }
            result[size++] = grade / 10;
            result[size++] = grade % 10;
        } else {
            if (size >= capacity) {
                capacity *= 2;
                result = realloc(result, sizeof(int) * capacity);
            }
            result[size++] = grade;
        }
        elf1 = (elf1 + 1 + result[elf1]) % size;
        elf2 = (elf2 + 1 + result[elf2]) % size;
    }
    for (int i = input; i < input + 10; i++) printf("%d", result[i]);
    free(result);
    printf("\n");
}

int check(int input,int inputLen, int* result,int size) {
    int check = 0;
    for (int i = 0; i < inputLen; i++) {
        check = check*10+result[size-inputLen+i];
    }
    return check != input;
}

void solvepart2(int input) {
    int capacity = 30000000;
    int* result = malloc(sizeof(int) * capacity);
    result[0] = 3;
    result[1] = 7;
    int size = 2;
    int elf1 = 0;
    int elf2 = 1;

    while (1) {
        int grade = result[elf1] + result[elf2];

        if (grade >= 10) {
            if (size + 2 >= capacity) { capacity *= 2; result = realloc(result, sizeof(int) * capacity); }
            result[size++] = grade / 10;
            if (size >= 6 && !check(input, 6, result, size)) { printf("Result: %d\n", size - 6); free(result); return; }
            result[size++] = grade % 10;
            if (size >= 6 && !check(input, 6, result, size)) { printf("Result: %d\n", size - 6); free(result); return; }
        } else {
            if (size + 1 >= capacity) { capacity *= 2; result = realloc(result, sizeof(int) * capacity); }
            result[size++] = grade;
            if (size >= 6 && !check(input, 6, result, size)) { printf("Result: %d\n", size - 6); free(result); return; }
        }

        elf1 = (elf1 + 1 + result[elf1]) % size;
        elf2 = (elf2 + 1 + result[elf2]) % size;
    }
}
int main(void) {
    printf("Test 9: \n");   solvepart1(9);
    printf("Test 5: \n");   solvepart1(5);
    printf("Partie 1 : \n");solvepart1(652601);
    printf("Partie 2: \n");solvepart2(652601);
    return 0;
}