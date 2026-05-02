
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "utilities.h"
#include "registerOperation.h"

// ── Opcodes ──────────────────────────────────────────────────────────────────

typedef void (*op_fn)(int*, int*);

static const char *OP_NAMES[] = {
    "addr","addi","mulr","muli",
    "banr","bani","borr","bori",
    "setr","seti","gtir","gtri",
    "gtrr","eqir","eqri","eqrr"
};

static const op_fn OP_FNS[] = {
    addr, addi, mulr, muli,
    banr, bani, borr, bori,
    setr, seti, gtir, gtri,
    gtrr, eqir, eqri, eqrr
};

#define NB_OPS 16

static op_fn find_op(const char *name)
{
    for (int i = 0; i < NB_OPS; i++)
        if (!strcmp(OP_NAMES[i], name))
            return OP_FNS[i];
    fprintf(stderr, "Opcode inconnu : %s\n", name);
    exit(1);
}

// ── Structures ───────────────────────────────────────────────────────────────

typedef struct {
    op_fn fn;
    int   ins[4]; // ins[0]=ignoré, ins[1]=a, ins[2]=b, ins[3]=c
    char  op_name[8];
} Instr;

// ── Parsing ──────────────────────────────────────────────────────────────────

static int   ip_reg   = -1;
static Instr prog[1024];
static int   prog_len = 0;

static void parse(char **lines, int count)
{
    for (int i = 0; i < count; i++) {
        char *line = lines[i];
        if (!line || line[0] == '\0') continue;

        if (line[0] == '#') {
            sscanf(line, "#ip %d", &ip_reg);
            continue;
        }

        char op[8];
        int a, b, c;
        if (sscanf(line, "%7s %d %d %d", op, &a, &b, &c) != 4) continue;

        Instr *ins    = &prog[prog_len++];
        ins->fn       = find_op(op);
        strncpy(ins->op_name, op, 7);
        ins->op_name[7] = '\0';

        // Format attendu par tes fonctions : r[ins[3]] = f(r[ins[1]], ins[2])
        ins->ins[0] = 0; // ignoré
        ins->ins[1] = a;
        ins->ins[2] = b;
        ins->ins[3] = c;
    }

    if (ip_reg < 0) {
        fprintf(stderr, "Erreur : directive #ip introuvable.\n");
        exit(1);
    }
}

// ── Recherche de l'instruction clé ───────────────────────────────────────────
//
// Le programme s'arrête uniquement quand un eqrr compare un registre à r0.

static int find_halt_instr(int *cmp_reg_out)
{
    for (int i = 0; i < prog_len; i++) {
        if (!strcmp(prog[i].op_name, "eqrr")) {
            int a = prog[i].ins[1], b = prog[i].ins[2];
            if (a == 0) { *cmp_reg_out = b; return i; }
            if (b == 0) { *cmp_reg_out = a; return i; }
        }
    }
    return -1;
}

// ── Table de hachage (partie 2 — détection de cycle) ────────────────────────

#define HASH_SIZE (1 << 22)   // ~4M entrées
#define HASH_EMPTY (-1)

static int *seen_table = NULL;

static void seen_init(void)
{
    seen_table = malloc(HASH_SIZE * sizeof(int));
    if (!seen_table) { perror("malloc"); exit(1); }
    memset(seen_table, 0xFF, HASH_SIZE * sizeof(int)); // -1 partout
}

static void seen_free(void) { free(seen_table); seen_table = NULL; }

static int seen_insert(int v)
{
    // Retourne 1 si déjà vu, 0 sinon
    unsigned int h = (unsigned int)v;
    h = ((h >> 16) ^ h) * 0x45d9f3b;
    h = ((h >> 16) ^ h) * 0x45d9f3b;
    h =  (h >> 16) ^ h;
    unsigned int idx = h & (HASH_SIZE - 1);

    while (seen_table[idx] != HASH_EMPTY) {
        if (seen_table[idx] == v) return 1;
        idx = (idx + 1) & (HASH_SIZE - 1);
    }
    seen_table[idx] = v;
    return 0;
}

// ── Émulateur ────────────────────────────────────────────────────────────────

static int run(int part)
{
    int cmp_reg = -1;
    int halt_ip = find_halt_instr(&cmp_reg);

    if (halt_ip < 0) {
        fprintf(stderr, "Instruction eqrr/r0 introuvable.\n");
        exit(1);
    }

    int regs[6] = {0, 0, 0, 0, 0, 0};
    int last     = -1;

    if (part == 2) seen_init();

    while (1) {
        int ip = regs[ip_reg];
        if (ip < 0 || ip >= prog_len) break;

        if (ip == halt_ip) {
            int candidate = regs[cmp_reg];

            if (part == 1)
                return candidate;

            // Partie 2 : cycle détecté ?
            if (seen_insert(candidate)) {
                seen_free();
                return last;
            }
            last = candidate;
        }

        Instr *ins = &prog[ip];
        ins->fn(regs, ins->ins);
        regs[ip_reg]++;
    }

    if (part == 2) seen_free();
    return last;
}

// ── Main ─────────────────────────────────────────────────────────────────────

int main(int argc, char **argv)
{
    const char *filename = (argc > 1) ? argv[1] : "input.txt";

    int    count = 0;
    char **lines = extractLines(filename, &count);

    parse(lines, count);
    free_lines(lines);

    printf("Partie 1 : %d\n", run(1));
    printf("Partie 2 : %d\n", run(2));

    return 0;
}
