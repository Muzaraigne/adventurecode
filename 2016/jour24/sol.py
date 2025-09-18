# -*- coding: utf-8 -*-
from collections import deque
from itertools import permutations

def objective(data):
    res = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            key = data[i][j]
            if key not in '.#':
                res[key] = (i, j)
    return res

def bfs_shortest_path(data, start, target):
    visited = set()
    queue = deque([(start[0], start[1], 0)])
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == target:
            return steps

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]):
                continue
            if data[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return float("inf")

def all_pairs_shortest(data, objectives):
    """Precompute distances between all objectives."""
    dists = {}
    keys = list(objectives.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            dist = bfs_shortest_path(data, objectives[a], objectives[b])
            dists[(a, b)] = dist
            dists[(b, a)] = dist
    return dists

def min_steps(data, startpoint='0', return_to_start=False):
    obj = objective(data)
    dists = all_pairs_shortest(data, obj)

    keys = list(obj.keys())
    keys.remove(startpoint)

    best = float("inf")
    for perm in permutations(keys):
        total = 0
        cur = startpoint
        for nxt in perm:
            total += dists[(cur, nxt)]
            cur = nxt
        if return_to_start:  # part 2
            total += dists[(cur, startpoint)]
        best = min(best, total)
    return best

if __name__ == "__main__":
    print("--- Jour 24 : Solution ---")
    with open("./2016/jour24/input.txt", "r") as f:
        data = [list(d) for d in f.read().splitlines()]

    with open("./2016/jour24/test.txt", "r") as f:
        data_test = [list(d) for d in f.read().splitlines()]

    print("Test (part1):", min_steps(data_test))
    print("Test (part2):", min_steps(data_test, return_to_start=True))
    print("Input (part1):", min_steps(data))
    print("Input (part2):", min_steps(data, return_to_start=True))
