#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"

// --- OPTIMISATION : Table de Hachage (HashSet) ---
// Permet de vérifier si un nombre existe en temps constant O(1)
// au lieu de parcourir tout le tableau O(N).

#define HASH_CAPACITY 200003 // Nombre premier pour limiter les collisions

typedef struct Node {
    int value;
    struct Node* next;
} Node;

typedef struct {
    Node* buckets[HASH_CAPACITY];
} HashSet;

// Fonction de hachage simple
unsigned int hash(int value) {
    return (abs(value)) % HASH_CAPACITY;
}

// Vérifie si une valeur est déjà dans l'ensemble
int set_contains(HashSet* set, int value) {
    unsigned int index = hash(value);
    Node* current = set->buckets[index];
    while (current != NULL) {
        if (current->value == value) return 1;
        current = current->next;
    }
    return 0;
}

// Ajoute une valeur dans l'ensemble
void set_add(HashSet* set, int value) {
    unsigned int index = hash(value);
    Node* new_node = malloc(sizeof(Node));
    if (new_node == NULL) exit(EXIT_FAILURE);

    new_node->value = value;
    new_node->next = set->buckets[index]; // Insertion en tête de liste
    set->buckets[index] = new_node;
}

// Nettoie la mémoire utilisée par la table
void set_free(HashSet* set) {
    for (int i = 0; i < HASH_CAPACITY; i++) {
        Node* current = set->buckets[i];
        while (current != NULL) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(set);
}
// --- FIN OPTIMISATION ---

int sum(char** lines) {
    int total = 0;
    for (int i = 0; lines[i] != NULL; i++) {
        total += atoi(lines[i]);
    }
    return total;
}

int part2(char** lines) {
    int frequency = 0;

    // Utilisation de calloc pour initialiser tous les buckets à NULL
    HashSet* seen_frequencies = calloc(1, sizeof(HashSet));
    if (!seen_frequencies) return -1;

    // La fréquence initiale 0 compte comme "vue"
    set_add(seen_frequencies, 0);

    while (1) { // Boucle infinie jusqu'à trouver le doublon
        for (int i = 0; lines[i] != NULL; i++) {
            frequency += atoi(lines[i]);

            // Vérification instantanée (O(1))
            if (set_contains(seen_frequencies, frequency)) {
                int result = frequency;
                set_free(seen_frequencies); // Nettoyage propre
                return result;
            }

            set_add(seen_frequencies, frequency);
        }
    }
}

int main(void) {
    char** input = extractLines("input.txt");
    if (input == NULL) return EXIT_FAILURE;

    char* test_input[] = {"+1", "-2", "+3", "+1", NULL};
    printf("Test jour 1 partie 1: %d\n", sum(test_input));

    printf("Solution jour 1 partie 1: %d\n", sum(input));
    printf("Solution jour 1 partie 2: %d\n", part2(input));

    free_lines(input);
    return 0;
}
