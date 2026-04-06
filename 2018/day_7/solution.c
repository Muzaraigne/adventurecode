#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utilities.h"

typedef struct Node {
    char name;
    int exists;          // 0: inexistant/fini, 1: disponible, 2: en cours
    int in_degree;
    char children[26];
    int num_children;
} Node;

typedef struct {
    char task;           // Nom de la tâche (ex: 'A'), 0 si libre
    int remaining_time;
} Worker;

Node graph[26];

// --- Fonctions de parsing et sélection (inchangées ou presque) ---

void parseInput(char** lines) {
    for (int i = 0; i < 26; i++) {
        graph[i].name = 'A' + i;
        graph[i].exists = 0;
        graph[i].in_degree = 0;
        graph[i].num_children = 0;
    }

    for (int i = 0; lines[i] != NULL; i++) {
        char parent, child;
        if (sscanf(lines[i], "Step %c must be finished before step %c can begin.", &parent, &child) == 2) {
            int p_idx = parent - 'A';
            int c_idx = child - 'A';
            graph[p_idx].exists = 1;
            graph[c_idx].exists = 1;
            graph[p_idx].children[graph[p_idx].num_children++] = child;
            graph[c_idx].in_degree++;
        }
    }
}

// Pour la partie 2, on sélectionne mais on marque "en cours" (2)
Node* selectNextAvailableTask() {
    for (int i = 0; i < 26; i++) {
        if (graph[i].exists == 1 && graph[i].in_degree == 0) {
            graph[i].exists = 2; // En cours
            return &graph[i];
        }
    }
    return NULL;
}

// --- Logique Partie 2 ---

int solvePart2(int num_workers, int base_time) {
    Worker workers[num_workers];
    for (int i = 0; i < num_workers; i++) {
        workers[i].task = 0;
        workers[i].remaining_time = 0;
    }

    int total_time = 0;
    int total_tasks = 0;
    for (int i = 0; i < 26; i++) if (graph[i].exists) total_tasks++;
    int tasks_finished = 0;

    while (tasks_finished < total_tasks) {
        // 1. Assigner des tâches aux workers libres
        for (int i = 0; i < num_workers; i++) {
            if (workers[i].task == 0) {
                Node* next = selectNextAvailableTask();
                if (next != NULL) {
                    workers[i].task = next->name;
                    workers[i].remaining_time = base_time + (next->name - 'A' + 1);
                }
            }
        }

        // 2. Avancer le temps (on cherche le prochain événement pour aller plus vite,
        // ou on avance seconde par seconde)
        total_time++;

        // 3. Décrémenter le temps et libérer les tâches finies
        for (int i = 0; i < num_workers; i++) {
            if (workers[i].task != 0) {
                workers[i].remaining_time--;
                if (workers[i].remaining_time == 0) {
                    char finished_task = workers[i].task;
                    Node* node = &graph[finished_task - 'A'];

                    // Libérer les enfants
                    for (int j = 0; j < node->num_children; j++) {
                        graph[node->children[j] - 'A'].in_degree--;
                    }

                    graph[finished_task - 'A'].exists = 0; // Terminée
                    workers[i].task = 0;
                    tasks_finished++;
                }
            }
        }
    }
    return total_time;
}

// --- Main ---

int main(void) {
    // On suppose que extractLines est défini ailleurs
    char** input = extractLines("input.txt", NULL);
    if (input == NULL) return EXIT_FAILURE;

    // Partie 1
    parseInput(input);
    char res_p1[30];
    // Attention : tri() consomme le graphe !
    // selectNextNode() de ta P1 doit être compatible.
    // printf("Resultat Partie 1: %s\n", tri(res_p1));

    // Partie 2
    // On re-parse car le graphe a été vidé par la Partie 1
    parseInput(input);
    int time = solvePart2(5, 60);
    printf("Resultat Partie 2: %d secondes\n", time);

    free_lines(input);
    return 0;
}