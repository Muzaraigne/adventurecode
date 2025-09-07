# -*- coding: utf-8 -*-

def cpy(x, y, registre):
    try:
        val = int(x)
    except ValueError:
        val = registre[x]
    registre[y] = val

def inc(x, registre):
    registre[x] += 1

def dec(x, registre):
    registre[x] -= 1

def jnz(x, y, registre):
    try:
        val = int(x)
    except ValueError:
        val = registre[x]
    try:
        jump = int(y)
    except ValueError:
        jump = registre[y]
    return jump if val != 0 else 1

def calcule(data, registre, debug=False):
    i = 0
    while i < len(data):
        inst = data[i]
        op = inst[0]

        if debug:
            print(f"{i:03d}: {inst} | {registre}")

        if op == "cpy":
            cpy(inst[1], inst[2], registre)
            i += 1
        elif op == "inc":
            inc(inst[1], registre)
            i += 1
        elif op == "dec":
            dec(inst[1], registre)
            i += 1
        elif op == "jnz":
            i += jnz(inst[1], inst[2], registre)
        else:
            raise ValueError(f"Instruction inconnue : {op}")

    return registre

def test():
    instru = [
        ['cpy', '41', 'a'],
        ['inc', 'a'],
        ['inc', 'a'],
        ['dec', 'a'],
        ['jnz', 'a', '2'],
        ['dec', 'a'],
    ]
    result = calcule(instru, {'a': 0, 'b': 0, 'c': 0, 'd': 0})
    if result['a'] == 42:
        print("✅ Test OK : registre['a'] == 42")
    else:
        print("❌ Test FAILED : registre['a'] == ", result['a'])

def parse_input(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip().split() for line in f.readlines() if line.strip()]

if __name__ == "__main__":
    print("--- 🧠 Advent of Code 2016 - Jour 12 ---")
    print("--- Test interne ---")
    test()
    data = parse_input(".\\2016\\jour12\\input.txt")
    registre = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    
    result = calcule(data, registre.copy())
    print("Partie 1 : Le registre 'a' vaut", result['a'])
    result = calcule(data, registre.copy())
    print("Partie 2 : Le registre 'a' vaut", result['a'])

   
