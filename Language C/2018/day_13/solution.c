#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"

typedef struct {
    int x;
    int y;
} Point;
typedef struct {
    Point curentloc;
    Point movement;
    int nbIntersections;
    int alive ;
} Kart;

Kart newKart(int x, int y,int mx,int my) {
    Kart kart;
    kart.curentloc.x = x;
    kart.curentloc.y = y;
    kart.movement.x = mx;
    kart.movement.y = my;
    kart.nbIntersections = 0;
    kart.alive=1;
    return kart;
}

Point addPoints(Point a, Point b) {
    return (Point){a.x + b.x, a.y + b.y};
}

int compareKarts(Kart a,Kart b) {
    if (a.curentloc.y != b.curentloc.y)
        return a.curentloc.y - b.curentloc.y;
    return a.curentloc.x - b.curentloc.x;
}

void merge(Kart* arr,int left,int mid,int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    Kart* L = malloc(sizeof(Kart) * n1);
    Kart* R = malloc(sizeof(Kart) * n2);

    for (int i = 0; i < n1; i++) L[i]=arr[left + i];
    for (int i = 0; i < n2; i++) R[i]=arr[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (compareKarts(L[i],R[j])<=0)
            arr[k++]=L[i++];
        else
            arr[k++]=R[j++];
    }
    while (i < n1) arr[k++]=L[i++];
    while (j < n2) arr[k++]=R[j++];
    free(L);
    free(R);
}

void mergeSort(Kart* arr,int left,int right) {
    if (left >= right) return;
    int mid =left+(right-left)/2;
    mergeSort(arr,left,mid);
    mergeSort(arr,mid+1,right);
    merge(arr,left,mid,right);
}

int listKart(char** lines, Kart* karts) {
    int counter = 0;
    for (int i = 0; lines[i] != NULL; i++) {
        for (int j = 0; lines[i][j] != '\0'; j++) {
            switch (lines[i][j]) {
                case '<': karts[counter++] = newKart(j, i, -1,  0); break;
                case '>': karts[counter++] = newKart(j, i,  1,  0); break;
                case '^': karts[counter++] = newKart(j, i,  0, -1); break;
                case 'v': karts[counter++] = newKart(j, i,  0,  1); break;
                default: break;
            }
        }
    }
    return counter;
}
void rotateIntersection(Kart* kart) {
    int turn = kart->nbIntersections % 3;
    kart->nbIntersections++;
    int dx = kart->movement.x, dy = kart->movement.y;
    switch (turn) {
        case 0:
            kart->movement = (Point){ dy, -dx};
            break;
        case 1:
            break;
        case 2:
            kart->movement = (Point){-dy,  dx};
            break;
    }
}

void play(Kart* kart, char c) {
    switch (c) {

        case '+':
            rotateIntersection(kart);
            break;

        case '/':
            kart->movement = (Point){-kart->movement.y, -kart->movement.x};
            break;

        case '\\':
            kart->movement = (Point){ kart->movement.y,  kart->movement.x};
            break;

    }

    kart->curentloc = addPoints(kart->curentloc, kart->movement);
}



void solvePart1(char** lines) {
    Kart karts[200];
    int size = listKart(lines, karts);

    while (1) {
        mergeSort(karts, 0, size - 1);
        for (int i = 0; i < size; i++) {
            play(&karts[i], lines[karts[i].curentloc.y][karts[i].curentloc.x]);
            for (int j = 0; j < size; j++) {
                if (i == j) continue;
                if (karts[i].curentloc.x == karts[j].curentloc.x &&
                    karts[i].curentloc.y == karts[j].curentloc.y) {
                    printf("Resolution: %d,%d\n",
                           karts[i].curentloc.x, karts[i].curentloc.y);
                    return;
                    }
            }
        }
    }
}

void solvePart2(char** lines) {
    Kart karts[200];
    int size = listKart(lines, karts);
    int alive = size;
    while (alive >1) {
        mergeSort(karts, 0, size - 1);
        for (int i = 0; i < size; i++) {
            if (!karts[i].alive) {
                continue;
            }
            play(&karts[i], lines[karts[i].curentloc.y][karts[i].curentloc.x]);
            for (int j = 0; j < size; j++) {
                if (i == j) continue;
                if (!karts[j].alive) continue;
                if (karts[i].curentloc.x == karts[j].curentloc.x &&
                    karts[i].curentloc.y == karts[j].curentloc.y) {
                    karts[i].alive = 0;
                    alive--;
                    karts[j].alive = 0;
                    alive--;
                    }
            }

        }
    }

    for (int i = 0; i < size; i++) {
        if (karts[i].alive) {
            printf("Resolution: %d,%d\n",
                           karts[i].curentloc.x, karts[i].curentloc.y);
        }
    }
}


int main(void) {
	char** input = extractLines("input.txt",NULL);
	if (input == NULL) return EXIT_FAILURE;

    char** test = extractLines("../2018/day_13/test.txt", NULL);
    if (test == NULL) return EXIT_FAILURE;
    printf("Test: \n");
    solvePart1(test);
    printf("Partie 1: \n");
    solvePart1(input);

    char** test2 = extractLines("../2018/day_13/test2.txt", NULL);
    if (test2 == NULL) return EXIT_FAILURE;
    printf("Test Partie 2: \n");
    solvePart2(test2);
    printf("Partie 2: \n");
    solvePart2(input);
    free_lines(test2);

	free_lines(input);
    free_lines(test);
	return 0;
}
