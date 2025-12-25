# -*- coding: utf-8 -*-
import os
from collections import defaultdict, deque

def bridge_strength(components):
    graph = defaultdict(list)
    for a, b in components:
        graph[a].append(b)
        graph[b].append(a)
    max_strength = 0
    max_length = 0
    max_length_strength = 0
    stack = deque()
    stack.append((0, 0, set()))  # (current_port, current_strength, used_components)
    while stack:
        current_port, current_strength, used_components = stack.pop()
        if len(used_components) > max_length:
            max_length = len(used_components)
            max_length_strength = current_strength
        elif len(used_components) == max_length:
            max_length_strength = max(max_length_strength, current_strength)
        max_strength = max(max_strength, current_strength)
        for next_port in graph[current_port]:
            component = (min(current_port, next_port), max(current_port, next_port))
            if component not in used_components:
                new_used_components = used_components | {component}
                new_strength = current_strength + sum(component)
                stack.append((next_port, new_strength, new_used_components))
    return max_strength, max_length_strength

if __name__ == "__main__" :
    print("--- Jour 24 : Solution ---")
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    print("Partie 1 et 2 :")
    components = [tuple(map(int, line.split('/'))) for line in data]
    part1, part2 = bridge_strength(components)
    print(f"  - Résultat partie 1 : {part1}")
    print(f"  - Résultat partie 2 : {part2}")