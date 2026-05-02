#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utilities.h"

#define HASH_SIZE 200003

// -------- DIST MAP --------

typedef struct Node {
    int x, y;
    int dist;
    struct Node *next;
} Node;

Node* table[HASH_SIZE];

unsigned int hash(int x, int y) {
    return (unsigned int)((x * 73856093) ^ (y * 19349663)) % HASH_SIZE;
}

int get_dist(int x, int y) {
    Node *n = table[hash(x,y)];
    while (n) {
        if (n->x == x && n->y == y)
            return n->dist;
        n = n->next;
    }
    return -1;
}

void set_dist(int x, int y, int d) {
    unsigned int h = hash(x,y);
    Node *n = table[h];

    while (n) {
        if (n->x == x && n->y == y) {
            if (d < n->dist) n->dist = d;
            return;
        }
        n = n->next;
    }

    Node *new = malloc(sizeof(Node));
    new->x = x;
    new->y = y;
    new->dist = d;
    new->next = table[h];
    table[h] = new;
}

// -------- POSITION SET --------

typedef struct Pos {
    int x, y;
    struct Pos *next;
} Pos;

Pos* add_pos(Pos *set, int x, int y) {
    for (Pos *p = set; p; p = p->next)
        if (p->x == x && p->y == y)
            return set;

    Pos *n = malloc(sizeof(Pos));
    n->x = x;
    n->y = y;
    n->next = set;
    return n;
}

Pos* copy_set(Pos *set) {
    Pos *res = NULL;
    for (Pos *p = set; p; p = p->next)
        res = add_pos(res, p->x, p->y);
    return res;
}

Pos* merge(Pos *a, Pos *b) {
    for (Pos *p = b; p; p = p->next)
        a = add_pos(a, p->x, p->y);
    return a;
}

void free_set(Pos *s) {
    while (s) {
        Pos *tmp = s;
        s = s->next;
        free(tmp);
    }
}

// -------- STACK --------

typedef struct Stack {
    Pos *start;
    Pos *accum;
    struct Stack *next;
} Stack;

Stack* push(Stack *s, Pos *start) {
    Stack *n = malloc(sizeof(Stack));
    n->start = copy_set(start);
    n->accum = NULL;
    n->next = s;
    return n;
}

Stack* pop(Stack *s, Pos **start, Pos **accum) {
    Stack *tmp = s;
    *start = tmp->start;
    *accum = tmp->accum;
    s = s->next;
    free(tmp);
    return s;
}

// -------- MAIN --------

int main(void) {
    char **lines = extractLines("input.txt", NULL);
    if (!lines || !lines[0]) return 1;

    char *p = lines[0];
    if (*p == '^') p++;

    Pos *current = NULL;
    current = add_pos(current, 0, 0);
    set_dist(0, 0, 0);

    Stack *stack = NULL;

    while (*p && *p != '$') {
        char c = *p++;

        if (c=='N'||c=='S'||c=='E'||c=='W') {
            Pos *next = NULL;

            for (Pos *pos = current; pos; pos = pos->next) {
                int x = pos->x, y = pos->y;

                if (c=='N') y++;
                if (c=='S') y--;
                if (c=='E') x++;
                if (c=='W') x--;

                int d = get_dist(pos->x, pos->y) + 1;
                int old = get_dist(x, y);

                if (old == -1 || d < old)
                    set_dist(x, y, d);

                next = add_pos(next, x, y);
            }

            free_set(current);
            current = next;
        }

        else if (c == '(') {
            stack = push(stack, current);
        }

        else if (c == '|') {
            stack->accum = merge(stack->accum, current);
            free_set(current);
            current = copy_set(stack->start);
        }

        else if (c == ')') {
            Pos *start, *accum;
            stack = pop(stack, &start, &accum);

            accum = merge(accum, current);

            free_set(current);
            current = accum;

            free_set(start);
        }
    }

    int max = 0, count1000 = 0;

    for (int i = 0; i < HASH_SIZE; i++) {
        Node *n = table[i];
        while (n) {
            if (n->dist > max) max = n->dist;
            if (n->dist >= 1000) count1000++;
            n = n->next;
        }
    }

    printf("Partie 1 : %d\n", max);
    printf("Partie 2 : %d\n", count1000);

    free_lines(lines);
    return 0;
}