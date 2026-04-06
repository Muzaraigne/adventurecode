# -*- coding: utf-8 -*- 
def decode_max(data) : 
    res =''
    for j in range(len(data[0])):
        dico = dict()
        for i in range(len(data)):
            c = data[i][j]
            if c in dico :
                dico[c] +=1
            else : 
                dico[c] = 1
        li = [(k,v) for k,v in dico.items()]
        li.sort(key=lambda x: (-x[1], x[0]))
        res += li[0][0]
    return res

def decode_min(data):
    res =''
    for j in range(len(data[0])):
        dico = dict()
        for i in range(len(data)):
            c = data[i][j]
            if c in dico :
                dico[c] +=1
            else : 
                dico[c] = 1
        li = [(k,v) for k,v in dico.items()]
        li.sort(key=lambda x: (x[1], x[0]))
        res += li[0][0]
    return res
if __name__ == "__main__" : 
    print("--- Jour 6 : Solution ---") 
    with open(".\\2016\\jour6\\input.txt","r") as f : 
        data = f.read().splitlines() 
        
    print(" Partie 1 : ")
    print("le message envoyé est ", decode_max(data))
    print("Partie 2 : ")
    print("le vrai message envoyé est",decode_min(data))
