#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"


typedef struct Node{
    int nbChild;
    int nbMetaData;
    struct Node** children;
    int* metaData;
}Node;

Node tree;
Node* parseNode(char** cursor){
    Node* node = malloc(sizeof(Node));
    char* end;
    node->nbChild = (int)strtol(*cursor, &end, 10);
    *cursor = end;
    node->nbMetaData = (int)strtol(*cursor, &end, 10);
    *cursor = end;

    // 2. Lire les enfants récursivement
    if (node->nbChild > 0) {
        node->children = malloc(sizeof(Node*) * node->nbChild);
        for (int i = 0; i < node->nbChild; i++) {
            node->children[i] = parseNode(cursor);
        }
    } else {
        node->children = NULL;
    }

    // 3. Lire les méta-données
    node->metaData = malloc(sizeof(int) * node->nbMetaData);
    for (int i = 0; i < node->nbMetaData; i++) {
        node->metaData[i] = (int)strtol(*cursor, &end, 10);
        *cursor = end;
    }

    return node;
}

int sumMetadata(Node* node) {
    int sum = 0;
    // Somme des metas du noeud actuel
    for (int i = 0; i < node->nbMetaData; i++) {
        sum += node->metaData[i];
    }
    // + Somme des enfants
    for (int i = 0; i < node->nbChild; i++) {
        sum += sumMetadata(node->children[i]);
    }
    return sum;
}

int sumData(Node* node) {
    int sum = 0;
    if(node->nbChild == 0){
        for (int i = 0; i < node->nbMetaData; i++) {
            sum += node->metaData[i];
        }
    }
    else{
        for (int i = 0; i < node->nbMetaData; i++) {
            int index = node->metaData[i];
            if(index > 0 && index <= node->nbChild){
                sum += sumData(node->children[index-1]);
            }
        }
    }
    return sum;
}

int main(void) {
    // Test
    char* test_str = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2";
    char* cursorTest = test_str;
    Node* rootTest = parseNode(&cursorTest);
    printf("Test P1: %d (attendu 138)\n", sumMetadata(rootTest));
    printf("Test P2: %d (attendu 66)\n", sumData(rootTest));


	char** input = extractLines("input.txt",NULL);
	if (input == NULL) return EXIT_FAILURE;

    char* cursor = input[0];
    Node* root = parseNode(&cursor);


    printf("Résultat Partie 1: %d\n", sumMetadata(root));
    printf("Résultat Partie 2: %d\n", sumData(root));

    free_lines(input);
	return 0;
}
