# -*- coding: utf-8 -*- 
import os

def transform(grid):
    length = len(grid)
    if length%2==0:
        size = 2
    else:
        size = 3
    new_grid = []
    for i in range(0, length, size):
        new_rows = []
        for j in range(0, length, size):
            block = [grid[x][j:j+size] for x in range(i, i+size)]
            block_str = '/'.join(block)
            if block_str in rules:
                new_block = rules[block_str]
            else:
                # Try all rotations and flips
                found = False
                for _ in range(4):
                    block = [''.join(row) for row in zip(*block[::-1])]  # Rotate 90 degrees
                    block_str = '/'.join(block)
                    if block_str in rules:
                        new_block = rules[block_str]
                        found = True
                        break
                    # Flip horizontally
                    block = [row[::-1] for row in block]
                    block_str = '/'.join(block)
                    if block_str in rules:
                        new_block = rules[block_str]
                        found = True
                        break
                    # Flip back to original before next rotation
                    block = [row[::-1] for row in block]
                if not found:
                    raise ValueError("No matching rule found for block: " + block_str)
            if not new_rows:
                new_rows = ['' for _ in range(len(new_block))]
            for k in range(len(new_block)):
                new_rows[k] += new_block[k]
        new_grid.extend(new_rows)
    grid[:] = new_grid

def count(grid):
    return sum(row.count('#') for row in grid)

def solve(number):
    base = ['.#.', '..#', '###']
    for _ in range(number):
        transform(base)
    return count(base)

if __name__ == "__main__" :
    print("--- Jour 21 : Solution ---")
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        rules=dict()
        for lignes in data:
            r,l = lignes.split(' => ')
            rules[r]=[motif for motif in l.split('/')]

    print("Partie 1 : ", solve(5))
    print("Partie 2 : ", solve(18))