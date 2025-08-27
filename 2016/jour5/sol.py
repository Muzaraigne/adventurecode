# -*- coding: utf-8 -*- 
from hashlib import md5

def md5_hash(s):
    return md5(s.encode()).hexdigest()

def find_lowest_number_whith_start(id_doors, leading_zeros,start):
    number = start 
    prefix = '0' * leading_zeros
    while True:
        hash_result = md5_hash(f"{id_doors}{number}")
        if hash_result.startswith(prefix) :
            return number
        number += 1

def find_code (entry):
    dep = 0
    res = ''
    for _ in range(8) :
        num = find_lowest_number_whith_start(entry,5, dep)
        dep = num+1
        chiffre = md5_hash(f'{entry}{num}')
        res += chiffre[5] 
    return res


def find_code2(entry) : 
    dep =0 
    res = [None,None,None,None,None,None,None,None]
    completion = 0
    while completion <8 : 
        num = find_lowest_number_whith_start(entry,5,dep)
        dep = num +1
        chiffre = md5_hash(f'{entry}{num}')
        if chiffre[5] in '01234567' :
            if res[int(chiffre[5])] == None :
                res[int(chiffre[5])] = chiffre[6]
                completion +=1
        
    return "".join(res)


if __name__ == "__main__" : 
    print("--- Jour 5 : Solution ---") 
    with open(".\\2016\\jour5\\input.txt","r") as f : 
       data = f.read().splitlines() 
    print("Partie 1 :  ")
    #print("Pour mon identifiant :", data, "le mdp de la salle : ",find_code(data[0]))

    print("Partie 2 :")
    print("Ladeuxieme prote a pour mdp : ",find_code2(data[0]))