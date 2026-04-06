# -*- coding: utf-8 -*- 
from collections import deque

def bfs_shortest_path(favorite_number, target):
    start = (1, 1)
    visited = set()
    queue = deque()
    
    # Chaque élément de la file sera (x, y, steps)
    queue.append((start[0], start[1], 0))
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == target:
            return steps

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            # On ignore les coordonnées négatives
            if nx < 0 or ny < 0:
                continue

            if is_open(nx, ny, favorite_number) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

def solve_part2(favorite_number,steps_max):
    start = (1, 1)
    visited = set()
    queue = deque()
    
    # Chaque élément de la file sera (x, y, steps)
    queue.append((start[0], start[1], 0))
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if steps > steps_max:
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            # On ignore les coordonnées négatives
            if nx < 0 or ny < 0:
                continue

            if is_open(nx, ny, favorite_number) and (nx, ny) not in visited:
                if steps + 1 <= steps_max:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))


    return len(visited)


def is_open(x, y, favorite_number):
    if x < 0 or y < 0:
        return False  # Tu ne peux pas aller dans les coordonnées négatives

    number = x*x + 3*x + 2*x*y + y + y*y + favorite_number
    ones = bin(number).count('1')
    return ones % 2 == 0

if __name__ == "__main__" : 
    print("--- Jour 13 : Solution ---") 
    entree = 1364 
    objectif = (31,39)
    entre_test = 10
    objectif_test = (7,4)

    print("Test : pour ce qu'on ous montre dans le sujet , je fait ", bfs_shortest_path(entre_test,objectif_test))
    print("Partie 1 : Le nombre de pas minimum pour atteindre l'objectif est de ",bfs_shortest_path(entree,objectif))
    print('Patie 2 : Le nombre de case visite en 50 pas est de ', solve_part2(entree,50))

