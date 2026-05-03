#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define TORCH   1
#define GEAR    2
#define NEITHER 0

/* Ajouter une marge au-delà de la cible pour les détours éventuels */
#define MARGIN  50
#define MAX_X   (6   + MARGIN)
#define MAX_Y   (770 + MARGIN)

typedef struct { int x, y; } Point;

/* Nœud pour la file de priorité (tas min) */
typedef struct { int cost, x, y, eq; } Node;

/* Tas min simple */
typedef struct {
    Node *data;
    int   size, cap;
} Heap;

static void heap_push(Heap *h, Node n) {
    if (h->size == h->cap) {
        h->cap = h->cap ? h->cap * 2 : 256;
        h->data = realloc(h->data, h->cap * sizeof(Node));
    }
    int i = h->size++;
    h->data[i] = n;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].cost <= h->data[i].cost) break;
        Node tmp = h->data[p]; h->data[p] = h->data[i]; h->data[i] = tmp;
        i = p;
    }
}

static Node heap_pop(Heap *h) {
    Node top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    for (;;) {
        int l = 2*i+1, r = 2*i+2, m = i;
        if (l < h->size && h->data[l].cost < h->data[m].cost) m = l;
        if (r < h->size && h->data[r].cost < h->data[m].cost) m = r;
        if (m == i) break;
        Node tmp = h->data[m]; h->data[m] = h->data[i]; h->data[i] = tmp;
        i = m;
    }
    return top;
}

/* Retourne 1 si l'équipement est compatible avec le terrain */
static int compatible(int terrain, int eq) {
    if (terrain == 0) return eq == GEAR  || eq == TORCH;
    if (terrain == 1) return eq == GEAR  || eq == NEITHER;
    if (terrain == 2) return eq == TORCH || eq == NEITHER;
    return 0;
}

/* Construit la grille d'érosion brute (pas encore % 3).
   Retourne un tableau alloué MAX_Y * MAX_X que l'appelant doit libérer. */
static int *build_erosion(Point target, int depth) {
    int *ero = malloc(MAX_Y * MAX_X * sizeof(int));
    if (!ero) return NULL;

    for (int y = 0; y < MAX_Y; y++) {
        for (int x = 0; x < MAX_X; x++) {
            long geo;
            if ((x == 0 && y == 0) || (x == target.x && y == target.y)) {
                geo = 0;
            } else if (y == 0) {
                geo = (long)x * 16807;
            } else if (x == 0) {
                geo = (long)y * 48271;
            } else {
                geo = (long)ero[y * MAX_X + (x-1)] * ero[(y-1) * MAX_X + x];
            }
            /* On stocke l'érosion brute (nécessaire pour le calcul géologique) */
            ero[y * MAX_X + x] = (int)((geo + depth) % 20183);
        }
    }
    return ero;
}

static int part1(const int *ero, Point target) {
    int risk = 0;
    for (int y = 0; y <= target.y; y++)
        for (int x = 0; x <= target.x; x++)
            risk += ero[y * MAX_X + x] % 3;
    return risk;
}

static int part2(const int *ero, Point target) {
    /* dist[y][x][eq] = coût minimal pour atteindre (x,y) avec équipement eq */
    static int dist[MAX_Y][MAX_X][3];
    for (int y = 0; y < MAX_Y; y++)
        for (int x = 0; x < MAX_X; x++)
            for (int e = 0; e < 3; e++)
                dist[y][x][e] = INT_MAX;

    Heap h = {0};
    dist[0][0][TORCH] = 0;
    heap_push(&h, (Node){0, 0, 0, TORCH});

    const int dx[] = {0, 0, 1, -1};
    const int dy[] = {1, -1, 0, 0};

    while (h.size) {
        Node cur = heap_pop(&h);
        if (cur.cost > dist[cur.y][cur.x][cur.eq]) continue;  /* périmé */

        /* Changement d'équipement (coût 7) */
        for (int e = 0; e < 3; e++) {
            if (e == cur.eq) continue;
            if (!compatible(ero[cur.y * MAX_X + cur.x] % 3, e)) continue;
            int nc = cur.cost + 7;
            if (nc < dist[cur.y][cur.x][e]) {
                dist[cur.y][cur.x][e] = nc;
                heap_push(&h, (Node){nc, cur.x, cur.y, e});
            }
        }

        /* Déplacement (coût 1) */
        for (int i = 0; i < 4; i++) {
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            if (nx < 0 || nx >= MAX_X || ny < 0 || ny >= MAX_Y) continue;
            if (!compatible(ero[ny * MAX_X + nx] % 3, cur.eq)) continue;
            int nc = cur.cost + 1;
            if (nc < dist[ny][nx][cur.eq]) {
                dist[ny][nx][cur.eq] = nc;
                heap_push(&h, (Node){nc, nx, ny, cur.eq});
            }
        }
    }

    free(h.data);
    return dist[target.y][target.x][TORCH];
}

static void solve(Point target, int depth, const char *label) {
    int *ero = build_erosion(target, depth);
    if (!ero) { fprintf(stderr, "alloc failed\n"); return; }

    printf("[%s] Partie 1 : %d\n", label, part1(ero, target));
    printf("[%s] Partie 2 : %d\n", label, part2(ero, target));

    free(ero);
}

int main(void) {
    solve((Point){10,  10},  510, "test ");  /* attendu : 114, 45 */
    solve((Point){ 6, 770}, 4845, "input");
    return 0;
}