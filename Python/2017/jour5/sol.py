# -*- coding: utf-8 -*- 

def compute (data):
  size = len(data)
  ind = 0 
  step = 0
  while size > ind : 
    bvalue = data[ind]
    data[ind] += 1
    ind += bvalue
    step +=1
  return step

def compute2 (data):
    size = len(data)
    ind = 0 
    step = 0
    while size > ind : 
      bvalue = data[ind]
      if bvalue <3:
        data[ind] += 1
      else :
        data[ind] -=1
      ind += bvalue
      step +=1
    return step

def test():
  li = [0,3,0,1,-3]
  b = compute(li.copy())
  c = compute2(li.copy())
  if b != 5 :
    print(f'error pas le bon resultat {b}') 
  if c != 10:
    print(f'error pas le bon resultat {c}') 
if __name__ == "__main__" : 
  print("--- Jour 5 : Solution ---") 
  with open(".\\2017\\jour5\\input.txt","r") as f : 
    data =[int(n) for n in  f.read().splitlines()] 
  test
  print(f'Partie 1 : Il faut {compute(data.copy())} mesures pour sortir')
  print(f'Partie 2 : Il faut {compute2(data.copy())} mesures pour sortir')