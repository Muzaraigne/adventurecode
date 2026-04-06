# -*- coding: utf-8 -*- 

def distance (x,y) : 
   return abs(x)+abs(y)

def calcule(data) :
    direction = 0
    x,y = 0,0
    for instruction in data : 
         turn = instruction[0]
         step = int(instruction[1:])
         if turn == "R" : 
              direction = (direction + 1) % 4
         else : 
              direction = (direction - 1) % 4
         if direction == 0 : 
              y += step
         elif direction == 1 : 
              x += step
         elif direction == 2 : 
              y -= step
         else : 
              x -= step
    return distance(x,y)

def calcule2(data) :
    direction = 0
    x,y = 0,0
    visited = set()
    visited.add((x,y))
    for instruction in data : 
         turn = instruction[0]
         step = int(instruction[1:])
         if turn == "R" : 
              direction = (direction + 1) % 4
         else : 
              direction = (direction - 1) % 4
         for _ in range(step) : 
              if direction == 0 : 
                   y += 1
              elif direction == 1 : 
                   x += 1
              elif direction == 2 : 
                   y -= 1
              else : 
                   x -= 1
              if (x,y) in visited : 
                   return distance(x,y)
              visited.add((x,y))
    return None

if __name__ == "__main__" : 
   print("--- Jour 1 : Solution ---") 
   with open(".\\2016\jour1\input.txt","r") as f : 
       data = f.read().strip().split(", ")
       print("Partie 1 : ",calcule(data))
       print("Partie 2 : ",calcule2(data))