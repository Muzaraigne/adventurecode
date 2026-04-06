# -*- coding: utf-8 -*- 
from collections import deque 

def compute(n):
    q = deque(range(1, n+1))
    while len(q) > 1:
        q.append(q.popleft())  
        q.popleft()            
    return q[0]

def compute_part2(n):
    # trouver la plus grande puissance de 3 <= n
    power = 1
    while power * 3 <= n:
        power *= 3
    l = n - power
    if l == 0:
        return n
    elif l <= power:
        return l
    else:
        return 2*l - power

if __name__ == "__main__" : 
    print("--- Jour 19 : Solution ---") 
    data = 3014603
    data_test = 5

    print(compute(5))
    print(compute_part2(5))
    print("Partie 1 : le dernier surviants est ",compute(data))
    print("Partie 1 : le dernier surviants est ",compute_part2(data))