//
// Created by Louis on 26/04/2026.
//

#include "registerOperation.h"




void addr(int* r, int* ins) { r[ins[3]] = r[ins[1]] + r[ins[2]]; }
void addi(int* r, int* ins) { r[ins[3]] = r[ins[1]] + ins[2]; }
void mulr(int* r, int* ins) { r[ins[3]] = r[ins[1]] * r[ins[2]]; }
void muli(int* r, int* ins) { r[ins[3]] = r[ins[1]] * ins[2]; }
void banr(int* r, int* ins) { r[ins[3]] = r[ins[1]] & r[ins[2]]; }
void bani(int* r, int* ins) { r[ins[3]] = r[ins[1]] & ins[2]; }
void borr(int* r, int* ins) { r[ins[3]] = r[ins[1]] | r[ins[2]]; }
void bori(int* r, int* ins) { r[ins[3]] = r[ins[1]] | ins[2]; }
void setr(int* r, int* ins) { r[ins[3]] = r[ins[1]]; }
void seti(int* r, int* ins) { r[ins[3]] = ins[1]; }
void gtir(int* r, int* ins) { r[ins[3]] = ins[1]  > r[ins[2]] ? 1 : 0; }
void gtri(int* r, int* ins) { r[ins[3]] = r[ins[1]] > ins[2]  ? 1 : 0; }
void gtrr(int* r, int* ins) { r[ins[3]] = r[ins[1]] > r[ins[2]] ? 1 : 0; }
void eqir(int* r, int* ins) { r[ins[3]] = ins[1]  == r[ins[2]] ? 1 : 0; }
void eqri(int* r, int* ins) { r[ins[3]] = r[ins[1]] == ins[2]  ? 1 : 0; }
void eqrr(int* r, int* ins) { r[ins[3]] = r[ins[1]] == r[ins[2]] ? 1 : 0; }
