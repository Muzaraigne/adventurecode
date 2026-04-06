# -*- coding: utf-8 -*- 
def cond(data):
    res = dict()
    for d in data:
        d = d.split(':')
        res[int(d[0])] = int(d[1])-1
    return res

def calcul(pos,profondeur) : 
  if pos%(profondeur*2)==0:
      return pos*(profondeur+1)
  else : 
      return 0
  
def compute(data) :
    res = 0
    for x,y in data.items() :
        res += calcul(x,y)
    return res

def delay (data): 
    i =0 
    control = 0 
    while control != len(data) : 
        control=0
        for x,y in data.items():
            control +=1
            if calcul(x+i,y) !=0 :
                i +=1
                control -= 1
                break
        
    return i

if __name__ == "__main__" : 
  print("--- Jour 13 : Solution ---") 
  with open(".\\2017\\jour13\\input.txt","r") as f : 
       
       data = cond(f.read().splitlines()) 
  with open(".\\2017\\jour13\\test.txt","r") as f : 
       dt = cond(f.read().splitlines())
  
  print("--Partie 1 : ---")
  print(f"Test: {compute(dt)==24}")
  print(f"La gravité du chemin est de {compute(data)}")

  print("--Partie 2 : ---")
  print(f"Test: {delay(dt)}")
  print(f"le plus petit temps a attendre avant de passer en sécurité : {delay(data)}")