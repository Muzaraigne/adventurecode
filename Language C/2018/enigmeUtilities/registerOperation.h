//
// Created by Louis on 26/04/2026.
//

#ifndef ADVENTURECODE_REGISTEROPERATION_H
#define ADVENTURECODE_REGISTEROPERATION_H

typedef void (*OpFunc)(int*, int*);


void addr(int* r, int* ins);
void addi(int* r, int* ins);
void mulr(int* r, int* ins);
void muli(int* r, int* ins);
void banr(int* r, int* ins);
void bani(int* r, int* ins);
void borr(int* r, int* ins);
void bori(int* r, int* ins);
void setr(int* r, int* ins);
void seti(int* r, int* ins);
void gtir(int* r, int* ins);
void gtri(int* r, int* ins);
void gtrr(int* r, int* ins);
void eqir(int* r, int* ins);
void eqri(int* r, int* ins);
void eqrr(int* r, int* ins);


#endif //ADVENTURECODE_REGISTEROPERATION_H
