# -*- coding: utf-8 -*- 
import re


def is_abba(data):
    for i in range(len(data)-3):
        if data[i]+data[i+1] == data[i+3]+data[i+2]:
            if data[i]==data[i+1]:
                continue
            else : 
                return True
    return False

def support_TLS(data):
    res = False
    for d in re.findall(r'\[.*?\]|[^\[\]]+', data) :
        if d.startswith('[') :
            if is_abba(d[1:len(d)-1]):
                return False
        else :
            if is_abba(d):
                res =True
    return res

def support_SSL(data):
    aba =set()
    bab = set()
    for d in re.findall(r'\[.*?\]|[^\[\]]+', data) :
        if d.startswith('[') :
            for  i in range(len(d) - 2):
                if d[i] == d[i + 2] and d[i] != d[i+1]:
                    c= d[i+1]+d[i]+d[i+1]
                    if c in aba :
                        return True
                    else:
                        bab.add(c)
        else :
            for  i in range(len(d) - 2):
                if d[i] == d[i + 2] and d[i] != d[i+1]:
                    c= d[i:i+3]
                    if c in bab :
                        return True
                    else:
                        aba.add(c)  
    return False

        
def sol_part1(data):
    res= []
    for i in data : 
        if support_TLS(i) :
            res.append(i)
    return res

def sol_part2(data):
    res =[]
    for i in data:
        if support_SSL(i):
            res.append(i)
    return res

if __name__ == "__main__" : 
    print("--- Jour 7 : Solution ---") 
    with open(".\\2016\\jour7\\input.txt","r") as f : 
        data = f.read().splitlines()

    data_test1 = [
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn'
    ] 
    data_test2 = [
        'aba[bab]xyz',
        'xyx[xyx]xyx',
        'aaa[kek]eke',
        'zazbz[bzb]cdb'
    ]
    res_test = sol_part1(data_test1)
    print("Sur les exemples qui nous on etait donnés, seuls",res_test,"sont des TLS valide")
    res1 = sol_part1(data)
    print("Partie 1 : il y a ",len(res1),"adresse IP qui supportent TLS ")
    print("sur la deuxieme partie les exemples vais sont ", sol_part2(data_test2))
    print("Partie 2 : il y a ",len(sol_part2(data)),"adresse IP qui supportent SSL" )
