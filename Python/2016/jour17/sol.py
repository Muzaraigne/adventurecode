# -*- coding: utf-8 -*- 
from hashlib import md5
from collections import deque 

def md5_hash(s):
    return md5(s.encode()).hexdigest()

def portes_ouvertes(passcode, chemin):
    code = md5_hash(passcode + chemin)
    ouvert = []
    directions = "UDLR"
    for i, c in enumerate(code[:4]):
        if c in "bcdef":
            ouvert.append(directions[i])
    return ouvert

def bfs (passcode):
    queue = deque()
    queue.append((0, 0, ''))
    dir  = {
        'U':(-1,0),
        'D':(1,0),
        'L':(0,-1),
        'R':(0,1)
    }
    

    while queue : 
        x, y,chemin= queue.popleft()

        if (x, y) == (3,3):
            return chemin
        possibility = portes_ouvertes(passcode,chemin)
        for p in possibility:
            dx,dy = dir[p]
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 3 and 0 <= ny <= 3:
                queue.append((nx, ny, chemin+p))


def bfs_longest(passcode):
    queue = deque()
    queue.append((0, 0, ''))
    dir  = {
        'U':(-1,0),
        'D':(1,0),
        'L':(0,-1),
        'R':(0,1)
    }
    max_len = 0

    while queue:
        x, y, chemin = queue.popleft()

        if (x, y) == (3,3):
            max_len = max(max_len, len(chemin))
            continue

        possibility = portes_ouvertes(passcode, chemin)
        for p in possibility:
            dx, dy = dir[p]
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 3 and 0 <= ny <= 3:
                queue.append((nx, ny, chemin+p))

    return max_len

if __name__ == "__main__" : 
    print("--- Jour 17 : Solution ---") 
    data  = 'qljzarfv'

    print("test de conformite au sujet : ")
    print(bfs('ihgpwlah')=='DDRRRD')
    print(bfs('kglvqrro') == 'DDUDRLRRUDRD')
    print(bfs('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

    print("Partie 1 : Le chemin le plus cours pour sortir du labyrinthe est : ",bfs(data))
    print("partie 2 : Le chemin le plus long possede ",bfs_longest(data))," pas"

