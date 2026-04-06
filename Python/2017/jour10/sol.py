# -*- coding: utf-8 -*-
from operator import xor

def rever(liste: list, ind: int, taille: int):
    rli = [liste[(ind + i) % len(liste)] for i in range(taille)]
    rli.reverse()
    for i in range(taille):
        liste[(ind + i) % len(liste)] = rli[i]
    return liste

def calcul(data, rg):
    li = [i for i in range(rg)]
    ind = 0 
    skipsize = 0
    for d in data:
        d = int(d)
        li = rever(li, ind, d)
        ind = (ind + d + skipsize) % rg
        skipsize += 1
    return li[0] * li[1]

def calcul_part2(data):
    ind = 0
    skipsize = 0
    li = list(range(256))
    for _ in range(64):
        for d in data:
            li = rever(li, ind, d)
            ind = (ind + d + skipsize) % 256
            skipsize += 1
    return li

def xor_li(liste):
    res = 0
    for i in liste:
        res = xor(res, i)
    return res

def hashage_dense(data):
    data = [ord(c) for c in data] + [17,31,73,47,23]

    li = calcul_part2(data.copy())

    dense_hash_dec = []
    for i in range(16):
        bloc = li[i*16:(i+1)*16]
        dense_hash_dec.append(xor_li(bloc))

    return ''.join(f'{n:02x}' for n in dense_hash_dec)

def test():
    # Cas de test pour la Partie 1
    rg = 5
    data = "3, 4, 1, 5"
    rep = calcul(data.split(','), rg)
    print(f"Pour les valeurs d'exemple (P1), mon code obtient: {rep}")

    # Cas de test pour la Partie 2
    test_data = [
        ("", "a258a2a20e6e44b3c076596200257404"),
        ("AoC 2017", "33efeb34ea91d6f53436d9f8ce22e49c"),
        ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
    ]
    
    print("\n--- Tests Part 2 ---")
    for input_str, expected in test_data:
        result = hashage_dense(input_str)
        print(f"Input: '{input_str}' -> {result} (Attendu: {expected}) {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    print("--- Jour 10 : Solution ---")
    with open(".\\2017\\jour10\\input.txt", "r") as f:
        data = f.read().strip()

    test()
    
    # Partie 1
    data_part1 = [int(i) for i in data.split(',')]
    res_part1 = calcul(data_part1, 256)
    print(f'\nPartie 1 : Le produit des deux premiers nombres de la liste est {res_part1}')

    # Partie 2
    
    res_part2 = hashage_dense(data)
    print(f'Partie 2 : Le Knot Hash final est {res_part2}')
