# python
# -*- coding: utf-8 -*-
import os


def get_value(registers, x):
    if x.lstrip('-').isdigit():
        return int(x)
    return registers[x]


def part1(data):
    registers = {chr(c): 0 for c in range(ord('a'), ord('h') + 1)}
    instructions = [line.split() for line in data]
    pc = 0
    mul_count = 0
    while 0 <= pc < len(instructions):
        inst = instructions[pc]
        cmd = inst[0]
        x = inst[1]
        y = inst[2] if len(inst) > 2 else None

        if cmd == 'set':
            registers[x] = get_value(registers, y)
        elif cmd == 'sub':
            registers[x] -= get_value(registers, y)
        elif cmd == 'mul':
            registers[x] *= get_value(registers, y)
            mul_count += 1
        elif cmd == 'jnz':
            if get_value(registers, x) != 0:
                pc += get_value(registers, y) - 1

        pc += 1

    return mul_count


def _is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def part2(data):
    instructions = [line.split() for line in data]
    base_b = None
    for inst in instructions:
        if inst[0] == 'set' and inst[1] == 'b' and inst[2].lstrip('-').isdigit():
            base_b = int(inst[2])
            break

    if base_b is None:
        # Fallback: unable to extract pattern, return 0 to signal failure
        return 0

    b = base_b * 100 + 100000
    c = b + 17000
    step = 17

    h = 0
    for n in range(b, c + 1, step):
        if not _is_prime(n):
            h += 1
    return h


if __name__ == "__main__":
    print("--- Jour 23 : Solution ---")
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    print("Partie 1 :", part1(data))
    print("Partie 2 :", part2(data))
