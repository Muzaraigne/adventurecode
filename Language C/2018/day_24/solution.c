#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "../../utilities.h"

#define MAX_GROUPS   50
#define MAX_TYPES    10
#define MAX_TYPE_LEN 32

typedef enum { IMMUNE_SYSTEM = 0, INFECTION = 1 } Army;

typedef struct {
    int   units;
    int   hp;
    int   attack;
    int   initiative;
    char  attack_type[MAX_TYPE_LEN];
    char  weaknesses[MAX_TYPES][MAX_TYPE_LEN];
    int   n_weak;
    char  immunities[MAX_TYPES][MAX_TYPE_LEN];
    int   n_immune;
    Army  army;
    int   alive;
} Group;

/* ------------------------------------------------------------------ */
/* Parsing helpers                                                      */
/* ------------------------------------------------------------------ */

static void str_tolower(char *s) {
    for (; *s; s++) *s = (char)tolower((unsigned char)*s);
}

/*
 * Parse the optional "(weak to ...; immune to ...)" block.
 * Returns pointer past the closing ')'.
 */
static const char *parse_modifiers(const char *p, Group *g) {
    if (*p != '(') return p;
    p++;
    while (*p && *p != ')') {
        while (*p == ' ') p++;
        int is_weak = 0;
        if (strncmp(p, "weak to", 7) == 0)   { is_weak = 1; p += 7; }
        else if (strncmp(p, "immune to", 9) == 0) { p += 9; }
        else { p++; continue; }
        while (*p == ' ') p++;
        /* read comma-separated damage types */
        while (*p && *p != ';' && *p != ')') {
            while (*p == ' ' || *p == ',') p++;
            char type[MAX_TYPE_LEN] = {0};
            int i = 0;
            while (*p && *p != ',' && *p != ';' && *p != ')' && *p != ' ')
                type[i++] = *p++;
            str_tolower(type);
            if (i == 0) continue;
            if (is_weak) {
                if (g->n_weak < MAX_TYPES)
                    strcpy(g->weaknesses[g->n_weak++], type);
            } else {
                if (g->n_immune < MAX_TYPES)
                    strcpy(g->immunities[g->n_immune++], type);
            }
            while (*p == ' ') p++;
        }
        if (*p == ';') p++;
    }
    if (*p == ')') p++;
    return p;
}

/*
 * Parse one group line, e.g.:
 *   18 units each with 729 hit points (weak to fire; immune to cold, slashing)
 *    with an attack that does 8 radiation damage at initiative 10
 */
static int parse_group(const char *line, Group *g, Army army) {
    memset(g, 0, sizeof(*g));
    g->army  = army;
    g->alive = 1;

    const char *p = line;
    /* units */
    g->units = (int)strtol(p, (char **)&p, 10);
    /* "units each with " */
    p = strstr(p, "with"); if (!p) return 0; p += 4;
    while (*p == ' ') p++;
    /* hp */
    g->hp = (int)strtol(p, (char **)&p, 10);
    /* skip "hit points" */
    p = strstr(p, "hit points"); if (!p) return 0; p += 10;
    while (*p == ' ') p++;
    /* optional modifier block */
    p = parse_modifiers(p, g);
    while (*p == ' ') p++;
    /* "with an attack that does " */
    p = strstr(p, "does"); if (!p) return 0; p += 4;
    while (*p == ' ') p++;
    /* attack damage */
    g->attack = (int)strtol(p, (char **)&p, 10);
    while (*p == ' ') p++;
    /* attack type */
    int i = 0;
    while (*p && *p != ' ') g->attack_type[i++] = *p++;
    g->attack_type[i] = '\0';
    str_tolower(g->attack_type);
    /* "damage at initiative " */
    p = strstr(p, "initiative"); if (!p) return 0; p += 10;
    while (*p == ' ') p++;
    g->initiative = (int)strtol(p, (char **)&p, 10);
    return 1;
}

/* ------------------------------------------------------------------ */
/* Combat logic                                                         */
/* ------------------------------------------------------------------ */

static int effective_power(const Group *g) {
    return g->units * g->attack;
}

static int damage_dealt(const Group *attacker, const Group *defender) {
    /* Check immunity */
    for (int i = 0; i < defender->n_immune; i++)
        if (strcmp(defender->immunities[i], attacker->attack_type) == 0)
            return 0;
    int base = effective_power(attacker);
    /* Check weakness */
    for (int i = 0; i < defender->n_weak; i++)
        if (strcmp(defender->weaknesses[i], attacker->attack_type) == 0)
            return base * 2;
    return base;
}

/* Comparator: target selection order (desc eff power, desc initiative) */
static int cmp_selection(const void *a, const void *b) {
    const Group *ga = *(const Group **)a;
    const Group *gb = *(const Group **)b;
    int ep_a = effective_power(ga), ep_b = effective_power(gb);
    if (ep_b != ep_a) return ep_b - ep_a;
    return gb->initiative - ga->initiative;
}

/* Comparator: attack order (desc initiative) */
static int cmp_initiative(const void *a, const void *b) {
    const Group *ga = *(const Group **)a;
    const Group *gb = *(const Group **)b;
    return gb->initiative - ga->initiative;
}

/*
 * Run one full combat with an optional boost for the immune system.
 * Returns:
 *   winning_army  written into *winner
 *   total units remaining
 *   -1 if stalemate (no kills in a round)
 */
static int simulate(Group *groups, int n, int boost, Army *winner) {
    /* Apply boost */
    for (int i = 0; i < n; i++)
        if (groups[i].army == IMMUNE_SYSTEM)
            groups[i].attack += boost;

    const Group *targets[MAX_GROUPS];  /* targets[i] = target chosen by group i */

    for (;;) {
        /* ---- Target selection ---- */
        /* Build ordered list of attackers */
        const Group *order[MAX_GROUPS];
        int alive_count = 0;
        for (int i = 0; i < n; i++)
            if (groups[i].alive && groups[i].units > 0)
                order[alive_count++] = &groups[i];
        qsort(order, alive_count, sizeof(order[0]), cmp_selection);

        int targeted[MAX_GROUPS] = {0}; /* indexed by group index in groups[] */
        memset(targets, 0, sizeof(targets));

        for (int ai = 0; ai < alive_count; ai++) {
            const Group *att = order[ai];
            int att_idx = (int)(att - groups);
            int best = -1;
            int best_dmg = 0, best_ep = 0, best_init = 0;

            for (int di = 0; di < n; di++) {
                const Group *def = &groups[di];
                if (!def->alive || def->units <= 0) continue;
                if (def->army == att->army) continue;
                if (targeted[di]) continue;
                int dmg = damage_dealt(att, def);
                if (dmg == 0) continue;
                int ep = effective_power(def);
                if (dmg > best_dmg ||
                    (dmg == best_dmg && ep > best_ep) ||
                    (dmg == best_dmg && ep == best_ep && def->initiative > best_init)) {
                    best = di; best_dmg = dmg; best_ep = ep; best_init = def->initiative;
                }
            }
            if (best >= 0) {
                targets[att_idx] = &groups[best];
                targeted[best] = 1;
            }
        }

        /* ---- Attack phase ---- */
        /* Build all-groups list sorted by initiative */
        const Group *init_order[MAX_GROUPS];
        int io_count = 0;
        for (int i = 0; i < n; i++)
            if (groups[i].alive && groups[i].units > 0)
                init_order[io_count++] = &groups[i];
        qsort(init_order, io_count, sizeof(init_order[0]), cmp_initiative);

        int total_killed = 0;
        for (int ai = 0; ai < io_count; ai++) {
            const Group *att = init_order[ai];
            if (!att->alive || att->units <= 0) continue;
            int att_idx = (int)(att - groups);
            const Group *def_c = targets[att_idx];
            if (!def_c) continue;
            int def_idx = (int)(def_c - groups);
            Group *def = &groups[def_idx];
            if (!def->alive || def->units <= 0) continue;

            int dmg = damage_dealt(att, def);
            int kills = dmg / def->hp;
            if (kills > def->units) kills = def->units;
            def->units -= kills;
            total_killed += kills;
            if (def->units <= 0) def->alive = 0;
        }

        /* Stalemate check */
        if (total_killed == 0) return -1;

        /* Check end condition */
        int has[2] = {0, 0};
        int count[2] = {0, 0};
        for (int i = 0; i < n; i++) {
            if (groups[i].alive && groups[i].units > 0) {
                has[(int)groups[i].army] = 1;
                count[(int)groups[i].army] += groups[i].units;
            }
        }
        if (!has[IMMUNE_SYSTEM] || !has[INFECTION]) {
            *winner = has[IMMUNE_SYSTEM] ? IMMUNE_SYSTEM : INFECTION;
            return count[IMMUNE_SYSTEM] + count[INFECTION];
        }
    }
}

/* ------------------------------------------------------------------ */
/* Input loading                                                        */
/* ------------------------------------------------------------------ */

static int load_groups(char **lines, int line_count, Group *groups) {
    int n = 0;
    Army current = IMMUNE_SYSTEM;
    for (int i = 0; i < line_count; i++) {
        char *l = lines[i];
        if (strncmp(l, "Immune System:", 14) == 0) { current = IMMUNE_SYSTEM; continue; }
        if (strncmp(l, "Infection:", 10) == 0)     { current = INFECTION;     continue; }
        if (strlen(l) < 5) continue;
        if (parse_group(l, &groups[n], current)) n++;
    }
    return n;
}

/* Deep-copy groups array */
static void copy_groups(const Group *src, Group *dst, int n) {
    memcpy(dst, src, n * sizeof(Group));
}

/* ------------------------------------------------------------------ */
/* Main                                                                 */
/* ------------------------------------------------------------------ */

int main(void) {
    int line_count = 0;
    char **lines = extractLines("input.txt", &line_count);
    if (!lines) return EXIT_FAILURE;

    Group base_groups[MAX_GROUPS];
    int n = load_groups(lines, line_count, base_groups);
    free_lines(lines);

    /* --- Part 1 --- */
    Group groups[MAX_GROUPS];
    copy_groups(base_groups, groups, n);
    Army winner;
    int result1 = simulate(groups, n, 0, &winner);
    printf("Part 1: %d\n", result1);

    /* --- Part 2: binary-search smallest boost for immune system to win --- */
    int lo = 1, hi = 100000, result2 = -1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        copy_groups(base_groups, groups, n);
        int res = simulate(groups, n, mid, &winner);
        if (res != -1 && winner == IMMUNE_SYSTEM) {
            result2 = res;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    printf("Part 2: %d\n", result2);

    return 0;
}