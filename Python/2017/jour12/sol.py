# -*- coding: utf-8 -*- 

import collections

def cond(data):
    res = dict()
    for d in data:
        temp = d.split('<->')
        res[int(temp[0])] = [int(i) for i in temp[1].split(',') if i.strip()]
    return res

def réseaux(data, cible):
    res = set()
    file = collections.deque([cible]) 
    res.add(cible) 

    while file: 
        f = file.popleft() 
        temp = data.get(f, []) 
        
        for t in temp:
            if t not in res:
                res.add(t) 
                file.append(t) 
                
    return res

def groups(data):
    nb = 0 
    dico = cond(data)
    all_prog = set(dico.keys())
    while all_prog : 
        start = next(iter(all_prog))
        temp = réseaux(dico,start)
        all_prog -= temp
        nb +=1
    return nb   
 
if __name__ == "__main__" : 
  print("--- Jour 12 : Solution ---") 
  with open(".\\2017\\jour12\\input.txt","r") as f : 
       data = f.read().splitlines() 
  with open(".\\2017\\jour12\\test.txt","r") as ti :
     dt = ti.read().splitlines()
  
  print(f"Test: {len(réseaux(cond(dt),0))==6}")
  print(f"Partie 1 : il y a {len(réseaux(cond(data),0))} tuyaux dans le groupe de 0 ")

  print(f"Test : {groups(dt)==2}")
  print(f"Partie 2 : il y a {groups(data)} groupes dans le reseaux")