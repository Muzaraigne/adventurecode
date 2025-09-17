# -*- coding: utf-8 -*-
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from jour12 import sol

def val(x, registre):
    try: 
        return int(x)
    except ValueError: 
        return registre[x]

def tgl(x, prog, registre, i):
    v = val(x, registre)
    target = i + v
    if 0 <= target < len(prog):
        instr = prog[target]
        if len(instr) == 2: 
            instr[0] = 'dec' if instr[0]=='inc' else 'inc'
        elif len(instr) == 3: 
            instr[0] = 'jnz' if instr[0]=='cpy' else 'cpy'
        prog[target] = instr

def calcule_opt(data, registre, debug=False):
    prog = [line.copy() for line in data]
    i = 0
    while i < len(prog):
        inst = prog[i]
        op = inst[0]
        if debug: 
            print(f"{i:03d}: {inst} | {registre}")

        if i + 2 < len(prog):
            a, b, c = prog[i:i+3]
            if a[0]=='dec' and b[0]=='inc' and c[0]=='jnz' and c[1]==a[1] and c[2]=='-2':
                registre[b[1]] += registre[a[1]]
                registre[a[1]] = 0
                i += 3
                continue

        if i + 5 < len(prog):
            p = prog[i:i+6]
            if (p[0][0]=='cpy' and p[1][0]=='inc' and p[2][0]=='dec' and
                p[3][0]=='jnz' and p[3][1]==p[2][1] and p[3][2]=='-2' and
                p[4][0]=='dec' and p[5][0]=='jnz' and p[5][1]==p[4][1] and p[5][2]=='-5'):
                registre[p[1][1]] += val(p[0][1], registre) * val(p[4][1], registre)
                registre[p[2][1]] = 0
                registre[p[4][1]] = 0
                i += 6
                continue

        if op == "cpy": 
            sol.cpy(inst[1], inst[2], registre)
            i += 1
        elif op == "inc": 
            sol.inc(inst[1], registre)
            i += 1
        elif op == "dec": 
            sol.dec(inst[1], registre)
            i += 1
        elif op == "jnz": 
            i += sol.jnz(inst[1], inst[2], registre)
        elif op == "tgl":
            tgl(inst[1], prog, registre, i)
            i += 1
        else: raise ValueError(f"Instruction inconnue : {op}")

    return registre

def parse_input(lines):
    return [line.strip().split() for line in lines if line.strip()]

if __name__ == "__main__":
    with open(".\\2016\\jour23\\input.txt","r") as f: 
        data = f.readlines()
    with open(".\\2016\\jour23\\test.txt","r") as fi:
        dt = fi.readlines()

    test_result = calcule_opt(parse_input(dt), {'a':0,'b':0,'c':0,'d':0})
    print(test_result['a']==3)

    r1 = sol.registre.copy()
    r1['a'] = 7
    print(f'Partie 1: {calcule_opt(parse_input(data), r1.copy())["a"]}')

    r2 = sol.registre.copy()
    r2['a'] = 12
    print(f'Partie 2: {calcule_opt(parse_input(data), r2.copy())["a"]}')
