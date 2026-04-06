# -*- coding: utf-8 -*-
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from jour12 import sol

def calcule(data, registre, debug=False, max_out=50):
    i = 0
    out_values = []
    while i < len(data):
        inst = data[i]
        op = inst[0]

        if debug:
            print(f"{i:03d}: {inst} | {registre}")

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
        elif op == "out":
            val = int(inst[1]) if inst[1].lstrip("-").isdigit() else registre[inst[1]]
            if val not in (0, 1):
                return False
            if out_values and val == out_values[-1]:  # must alternate
                return False
            out_values.append(val)
            if len(out_values) >= max_out:
                return True
            i += 1
        else:
            raise ValueError(f"Instruction inconnue : {op}")
    return False

def comput(data):
    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    while True:
        if calcule(data, reg.copy(), max_out=50):
            return reg["a"]
        reg["a"] += 1

def parse_input(lines):
    return [line.strip().split() for line in lines if line.strip()]

if __name__ == "__main__": 
    print("--- Jour 25 : Solution ---") 
    with open("./2016/jour25/input.txt","r") as f: 
        data = f.read().splitlines() 
    print("Partie 1 : le nombre minimal est :", comput(parse_input(data)))
