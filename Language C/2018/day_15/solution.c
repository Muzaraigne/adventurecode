#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../utilities.h"

#define MAX_UNITS 500
#define MAX_SIZE  100
#define INF 999999

char grid[MAX_SIZE][MAX_SIZE];
int rows, cols;

typedef struct {
    int hp;
    int attack;
    int x;
    int y;
    int equipe;
    int alive;
} Unit;

typedef struct {
    int x, y;
} Point;

Unit new_unit(int x, int y, int equipe, int elf_attack) {
    Unit unit;
    unit.hp = 200;
    unit.attack = (equipe == 'E') ? elf_attack : 3;
    unit.x = x;
    unit.y = y;
    unit.equipe = equipe;
    unit.alive = 1;
    return unit;
}

int compareUnits(const void* a, const void* b) {
    Unit* ua = (Unit*)a;
    Unit* ub = (Unit*)b;
    if (ua->y != ub->y) return ua->y - ub->y;
    return ua->x - ub->x;
}

int isOccupied(Unit* units, int nbUnits, int x, int y) {
    for (int i = 0; i < nbUnits; i++) {
        if (units[i].alive && units[i].x == x && units[i].y == y) return 1;
    }
    return 0;
}

int isWalkable(Unit* units, int nbUnits, int x, int y) {
    if (x < 0 || x >= cols || y < 0 || y >= rows) return 0;
    if (grid[y][x] == '#') return 0;
    if (isOccupied(units, nbUnits, x, y)) return 0;
    return 1;
}

void bfs(int startX, int startY, Unit* units, int nbUnits, int dist[MAX_SIZE][MAX_SIZE]) {
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++)
            dist[y][x] = -1;

    Point queue[MAX_SIZE * MAX_SIZE];
    int head = 0, tail = 0;

    dist[startY][startX] = 0;
    queue[tail++] = (Point){startX, startY};

    int dx[] = { 0, -1, 1, 0 };
    int dy[] = { -1, 0, 0, 1 };

    while (head < tail) {
        Point cur = queue[head++];
        for (int d = 0; d < 4; d++) {
            int nx = cur.x + dx[d];
            int ny = cur.y + dy[d];
            if (dist[ny][nx] == -1 && isWalkable(units, nbUnits, nx, ny)) {
                dist[ny][nx] = dist[cur.y][cur.x] + 1;
                queue[tail++] = (Point){nx, ny};
            }
        }
    }
}

Point firstStep(int fromX, int fromY, int targetX, int targetY, Unit* units, int nbUnits) {
    int dist[MAX_SIZE][MAX_SIZE];
    bfs(targetX, targetY, units, nbUnits, dist);

    int dx[] = { 0, -1, 1, 0 };
    int dy[] = { -1, 0, 0, 1 };

    Point best = { -1, -1 };
    int bestDist = INF;

    for (int d = 0; d < 4; d++) {
        int nx = fromX + dx[d];
        int ny = fromY + dy[d];
        if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && dist[ny][nx] != -1) {
            if (dist[ny][nx] < bestDist) {
                bestDist = dist[ny][nx];
                best = (Point){nx, ny};
            }
        }
    }
    return best;
}

int moveUnit(Unit* unit, Unit* units, int nbUnits) {
    int dx[] = { 0, -1, 1, 0 };
    int dy[] = { -1, 0, 0, 1 };

    for (int d = 0; d < 4; d++) {
        for (int i = 0; i < nbUnits; i++) {
            if (units[i].alive && units[i].equipe != unit->equipe) {
                if (unit->x + dx[d] == units[i].x && unit->y + dy[d] == units[i].y) return 0;
            }
        }
    }

    int dist[MAX_SIZE][MAX_SIZE];
    bfs(unit->x, unit->y, units, nbUnits, dist);

    Point target = { -1, -1 };
    int minD = INF;

    for (int i = 0; i < nbUnits; i++) {
        if (!units[i].alive || units[i].equipe == unit->equipe) continue;
        for (int d = 0; d < 4; d++) {
            int nx = units[i].x + dx[d];
            int ny = units[i].y + dy[d];
            if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && dist[ny][nx] != -1) {
                if (dist[ny][nx] < minD || (dist[ny][nx] == minD && (ny < target.y || (ny == target.y && nx < target.x)))) {
                    minD = dist[ny][nx];
                    target = (Point){nx, ny};
                }
            }
        }
    }

    if (target.x != -1) {
        Point step = firstStep(unit->x, unit->y, target.x, target.y, units, nbUnits);
        if (step.x != -1) {
            unit->x = step.x;
            unit->y = step.y;
            return 1;
        }
    }
    return 0;
}

void attackUnit(Unit* unit, Unit* units, int nbUnits) {
    int dx[] = { 0, -1, 1, 0 };
    int dy[] = { -1, 0, 0, 1 };
    int targetIdx = -1;
    int minHP = 999;

    for (int d = 0; d < 4; d++) {
        int nx = unit->x + dx[d];
        int ny = unit->y + dy[d];
        for (int i = 0; i < nbUnits; i++) {
            if (units[i].alive && units[i].equipe != unit->equipe && units[i].x == nx && units[i].y == ny) {
                if (units[i].hp < minHP) {
                    minHP = units[i].hp;
                    targetIdx = i;
                }
            }
        }
    }
    if (targetIdx != -1) {
        units[targetIdx].hp -= unit->attack;
        if (units[targetIdx].hp <= 0) units[targetIdx].alive = 0;
    }
}

int simulate(char** input, int total_lines, int elf_attack, int part2) {
    rows = total_lines;
    cols = (int)strlen(input[0]);
    Unit units[MAX_UNITS];
    int nbUnits = 0;

    for (int y = 0; y < rows; y++) {
        for (int x = 0; x < cols; x++) {
            grid[y][x] = input[y][x];
            if (grid[y][x] == 'G' || grid[y][x] == 'E') {
                units[nbUnits++] = new_unit(x, y, grid[y][x], elf_attack);
                grid[y][x] = '.';
            }
        }
    }

    int initial_elves = 0;
    for(int i=0; i<nbUnits; i++) if(units[i].equipe == 'E') initial_elves++;

    int rounds = 0;
    while (1) {
        qsort(units, nbUnits, sizeof(Unit), compareUnits);
        for (int i = 0; i < nbUnits; i++) {
            if (!units[i].alive) continue;

            int enemies_left = 0;
            for (int j = 0; j < nbUnits; j++)
                if (units[j].alive && units[j].equipe != units[i].equipe) enemies_left = 1;

            if (!enemies_left) goto end_battle;

            moveUnit(&units[i], units, nbUnits);
            attackUnit(&units[i], units, nbUnits);

            if (part2) {
                for (int j = 0; j < nbUnits; j++)
                    if (units[j].equipe == 'E' && !units[j].alive) return -1;
            }
        }
        rounds++;
    }

end_battle:;
    int total_hp = 0;
    for (int i = 0; i < nbUnits; i++) if (units[i].alive) total_hp += units[i].hp;
    return rounds * total_hp;
}

int main(void) {
    int tt = 0;
    char** input = extractLines("input.txt", &tt);
    if (!input) return EXIT_FAILURE;

    printf("Partie 1 : %d\n", simulate(input, tt, 3, 0));

    int attack = 4;
    while (1) {
        int res = simulate(input, tt, attack, 1);
        if (res != -1) {
            printf("Partie 2 (Attack %d) : %d\n", attack, res);
            break;
        }
        attack++;
    }

    free_lines(input);
    return 0;
}