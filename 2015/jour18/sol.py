# -*- coding: utf-8 -*- 
import copy



def voisin_on (x,y,data):
   on = 0
   for dx in [-1,0,1] :
      for dy in [-1,0,1] :
         if (dx != 0 or dy != 0) and 0 <= x+dx < len(data) and 0 <= y+dy < len(data[0]) :
            if data[x+dx][y+dy] == '#' :
               on += 1
   return on


def etape_conway (data) :
   new = copy.deepcopy(data)
   for i in range(len(data)) :
      for j in range(len(data[0])) :
         on = voisin_on(i,j,data)
         if data[i][j] == '#' and( on not in [2,3]) :
               new[i][j] = '.'
         if data[i][j] =='.' and on == 3 :
               new[i][j] = '#'
   return new

def simulerConway (data, n) :
   for _ in range(n) :
      data = etape_conway(data)
   return data

def simulerConwayCoinAllume (data, n) :
   data[0][0] = '#'
   data[0][-1] = '#'
   data[-1][0] = '#'
   data[-1][-1] = '#'
   for _ in range(n) :
      data = etape_conway(data)
      data[0][0] = '#'
      data[0][-1] = '#'
      data[-1][0] = '#'
      data[-1][-1] = '#'
   return data

def count_on (data) :
   return sum([ligne.count('#') for ligne in data])

if __name__ == "__main__" : 
   print("--- Jour 18 : Soluce ---")

   with open("2015/jour18/input.txt") as fichier : 
      lignes = fichier.read().split("\n")
      lignes = [list(ligne) for ligne in lignes]

   print("Partie 1 : il y a ", count_on(simulerConway(lignes, 100)))
   print("Partie 2 : il y a ", count_on(simulerConwayCoinAllume(lignes, 100)))
