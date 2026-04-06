# -*- coding: utf-8 -*- 

import string
Alphabet = string.ascii_lowercase


def standardisation_data(data) : 
    data = data.split('[')
    id = data[0].split('-')[-1]
    name = '-'.join(data[0].split('-')[:-1])
    checksum = data[1][:-1]
    return {
        'encrypt':name, 
        'id' : int(id), 
        'checksum' : checksum}

def nb_occ_dict(string) : 
    d = {}
    for c in string : 
        if c in d : 
            d[c] += 1
        else : 
            d[c] = 1
    return d

def is_valid(data) : 
    d = nb_occ_dict(data['encrypt'])
    d.pop('-', None)
    li = [(k,v) for k,v in d.items()]
    li.sort(key=lambda x: (-x[1], x[0]))
    checksum = ''.join([x[0] for x in li[:5]])
    return checksum == data['checksum']
def dechivre_cesar(data):
    shift = data['id'] % 26
    res = ""
    for c in data['encrypt'] : 
        if c == '-' : 
            res += ' '
        else : 
            res += Alphabet[(Alphabet.index(c) + shift) % 26]
    return res


if __name__ == "__main__" : 
    print("--- Jour 4 : Solution ---") 
    with open(".\\2016\\jour4\\input.txt","r") as f : 
       data = f.read().splitlines() 
    data = [standardisation_data(d) for d in data]
    res1 = sum([d['id'] for d in data if is_valid(d)])
    res2 = [(dechivre_cesar(d), d['id']) for d in data if is_valid(d)]
    print("Partie 1 :", res1, " : somme des id des salles valides")
    stock = [d for d in res2 if 'north' in d[0]]
    print("Partie 2 : la salle que l'on recherche est  ",stock[0] )