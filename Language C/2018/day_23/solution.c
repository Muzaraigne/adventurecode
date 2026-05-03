#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

#include "utilities.h"

typedef struct { int x, y, z, r; } Nanobot;

typedef struct {
    int x, y, z;
    int size;
    int count;
    int dist_to_origin;
} Cube;

typedef struct {
    Cube *data;
    int size, cap;
} PQ;

static int iabs(int a) { return a < 0 ? -a : a; }

int manhattan3(int x1, int y1, int z1, int x2, int y2, int z2) {
    return iabs(x1-x2) + iabs(y1-y2) + iabs(z1-z2);
}

/* Distance MINIMALE entre le cube et l'origine */
int dist_origin(Cube c) {
    /* Pour chaque axe : si l'intervalle [x, x+size-1] contient 0 → contrib 0 */
    int dx = 0, dy = 0, dz = 0;
    int cx2 = c.x + c.size - 1;
    int cy2 = c.y + c.size - 1;
    int cz2 = c.z + c.size - 1;
    if      (c.x > 0)  dx = c.x;
    else if (cx2 < 0)  dx = -cx2;          /* cube entièrement négatif */
    if      (c.y > 0)  dy = c.y;
    else if (cy2 < 0)  dy = -cy2;
    if      (c.z > 0)  dz = c.z;
    else if (cz2 < 0)  dz = -cz2;
    return dx + dy + dz;
}

int count_in_cube(Cube c, int n, Nanobot *bots) {
    int cnt = 0;
    int cx2 = c.x + c.size - 1;
    int cy2 = c.y + c.size - 1;
    int cz2 = c.z + c.size - 1;
    for (int i = 0; i < n; i++) {
        /* Distance Manhattan entre le nanobot et le cube (0 si dedans) */
        int d = 0;
        if      (bots[i].x < c.x)  d += c.x  - bots[i].x;
        else if (bots[i].x > cx2)  d += bots[i].x - cx2;
        if      (bots[i].y < c.y)  d += c.y  - bots[i].y;
        else if (bots[i].y > cy2)  d += bots[i].y - cy2;
        if      (bots[i].z < c.z)  d += c.z  - bots[i].z;
        else if (bots[i].z > cz2)  d += bots[i].z - cz2;
        if (d <= bots[i].r) cnt++;
    }
    return cnt;
}

/* Comparateur : count décroissant, puis dist_to_origin croissant */
static int better(Cube a, Cube b) {
    if (a.count != b.count) return a.count > b.count;
    return a.dist_to_origin < b.dist_to_origin;
}

void pq_push(PQ *pq, Cube c) {
    if (pq->size == pq->cap) {
        pq->cap = pq->cap ? pq->cap * 2 : 256;
        pq->data = realloc(pq->data, pq->cap * sizeof(Cube));
    }
    int i = pq->size++;
    pq->data[i] = c;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!better(pq->data[i], pq->data[p])) break;
        Cube tmp = pq->data[p]; pq->data[p] = pq->data[i]; pq->data[i] = tmp;
        i = p;
    }
}

Cube pq_pop(PQ *pq) {
    Cube top = pq->data[0];
    pq->data[0] = pq->data[--pq->size];
    int i = 0;
    for (;;) {
        int l = 2*i+1, r = 2*i+2, best = i;
        if (l < pq->size && better(pq->data[l], pq->data[best])) best = l;
        if (r < pq->size && better(pq->data[r], pq->data[best])) best = r;
        if (best == i) break;
        Cube tmp = pq->data[best]; pq->data[best] = pq->data[i]; pq->data[i] = tmp;
        i = best;
    }
    return top;
}

void solve(int n, Nanobot *bots) {
    /* Partie 1 */
    int max_r = -1, si = 0;
    for (int i = 0; i < n; i++)
        if (bots[i].r > max_r) { max_r = bots[i].r; si = i; }
    int p1 = 0;
    for (int i = 0; i < n; i++)
        if (manhattan3(bots[si].x, bots[si].y, bots[si].z,
                       bots[i].x,  bots[i].y,  bots[i].z) <= bots[si].r) p1++;
    printf("Partie 1 : %d\n", p1);

    /* Partie 2 : divide & conquer */
    int initial_size = 1;
    while (initial_size < 200000000) initial_size *= 2;  /* 268435456 */

    Cube root = {-initial_size, -initial_size, -initial_size, initial_size * 2, 0, 0};
    root.count = count_in_cube(root, n, bots);
    root.dist_to_origin = dist_origin(root);

    PQ pq = {0};
    pq_push(&pq, root);

    while (pq.size) {
        Cube cur = pq_pop(&pq);
        if (cur.size == 1) {
            printf("Partie 2 : %d\n", cur.dist_to_origin);
            break;
        }
        int ns = cur.size / 2;
        for (int i = 0; i < 8; i++) {
            Cube child = {
                cur.x + ((i & 1)      ? ns : 0),
                cur.y + (((i >> 1) & 1) ? ns : 0),  /* bit 1 */
                cur.z + (((i >> 2) & 1) ? ns : 0),  /* bit 2 */
                ns, 0, 0
            };
            child.count = count_in_cube(child, n, bots);
            child.dist_to_origin = dist_origin(child);
            pq_push(&pq, child);
        }
    }
    free(pq.data);
}

int main(void) {
    /* Lecture de l'input */
    char **lines = extractLines("input.txt", NULL);
    if (!lines || !lines[0]) return 1;
    int cursor =0;
    int cap = 1024, n = 0;
    Nanobot *bots = malloc(cap * sizeof(Nanobot));
    while (sscanf(lines[cursor++], " pos=<%d,%d,%d>, r=%d",
                  &bots[n].x, &bots[n].y, &bots[n].z, &bots[n].r) == 4) {
        if (++n == cap) { cap *= 2; bots = realloc(bots, cap * sizeof(Nanobot)); }
    }
    free_lines(lines);
    solve(n, bots);
    free(bots);
    return 0;
}