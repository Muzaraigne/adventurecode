#include <stdio.h>
#include <stdlib.h>

typedef struct List {
    int value;
    struct List *next;
    struct List *prev;
} List;

List* newList(int value) {
    List* node = (List*)malloc(sizeof(List));
    node->value = value;
    node->next = node;
    node->prev = node;
    return node;
}

List* addAfter(List* node, int value) {
    List* new_node = (List*)malloc(sizeof(List));
    new_node->value = value;

    new_node->next = node->next;
    new_node->prev = node;
    node->next->prev = new_node;
    node->next = new_node;

    return new_node;
}

long long play(int nbPlayer, int maxMarble) {
    long long* scores = (long long*)calloc(nbPlayer, sizeof(long long));

    List* current = newList(0);

    for (int m = 1; m <= maxMarble; m++) {
        if (m % 23 == 0) {
            int currentPlayer = m % nbPlayer;
            scores[currentPlayer] += m;

            for (int i = 0; i < 7; i++) current = current->prev;

            scores[currentPlayer] += current->value;
            List* toDelete = current;
            current = toDelete->next;
            toDelete->prev->next = toDelete->next;
            toDelete->next->prev = toDelete->prev;
            free(toDelete);
        } else {
            current = addAfter(current->next, m);
        }
    }

    long long highScore = 0;
    for (int i = 0; i < nbPlayer; i++) {
        if (scores[i] > highScore) highScore = scores[i];
    }

    free(scores);
    free(current);
    return highScore;
}

int main(void) {
    // Test avec l'exemple : 9 joueurs, jusqu'à la bille 25
    printf("Resultat Test (9, 25): %lld\n", play(9, 25));
    printf("Resultat (10, 1618): %lld\n", play(10, 1618));
    printf("Result Part 1 : %lld \n ",play(466,71436));
    printf("Result Part 2 : %lld \n ",play(466,7143600));

    return 0;
}