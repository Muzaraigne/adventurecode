# -*- coding: utf-8 -*-
import os
from malware import Virus, VirusResistAttempt

def simulate_virus(bursts, virus):
    for _ in range(bursts):
        virus.burst()
    return virus.infections

if __name__ == "__main__":
    print("--- Jour 22 : Solution ---")
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        grid = [[1 if ci == '#' else 0 for ci in c] for c in data]

        initial_infected = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    initial_infected.add((row, col))

    center = (len(grid) // 2, len(grid[0]) // 2)

    print("--- Partie 1 : Solution ---")
    res1 = set(initial_infected)
    result_part1 = simulate_virus(10000, Virus(res1, center))
    print(f"Nombre d'infections après 10000 bursts : {result_part1}")

    print("--- Partie 2 : Solution ---")
    res2 = set(initial_infected)
    result_part2 = simulate_virus(10000000, VirusResistAttempt(res2, center))
    print(f"Nombre d'infections après 10000000 bursts : {result_part2}")
