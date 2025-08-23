# -*- coding: utf-8 -*- 
def part1(data, critere) : 
   for (nom,attributs) in data :
      trouve = True
      cle = list(attributs.keys())
      valeur = list(attributs.values())
      i = 0
      while i < len(attributs) and trouve :
         if critere[cle[i]] != valeur[i] : 
            trouve = False
         i += 1
      if trouve : 
         return nom
   return None

def part2(data, critere) :
   for (nom,attributs) in data :
      trouve = True
      cle = list(attributs.keys())
      valeur = list(attributs.values())
      i = 0
      while i < len(attributs) and trouve :
         if cle[i] in ['cats','trees'] : 
            if critere[cle[i]] >= valeur[i] : 
               trouve = False
         elif cle[i] in ['pomeranians','goldfish'] : 
            if critere[cle[i]] <= valeur[i] : 
               trouve = False
         else : 
            if critere[cle[i]] != valeur[i] : 
               trouve = False
         i += 1
      if trouve : 
         return nom
   return None

if __name__ == "__main__" : 
   print("-- Jour 16 : Tanbte Sue (Solution) --")

   with open("2015/jour16/input.txt", "r") as fichier :
      lignes = fichier.read().splitlines()
      for i in range(0,len(lignes)): 
         t = lignes[i].replace(",","").replace(":","").split(" ")
         lignes[i] = (t[1], {t[2]:int(t[3]), t[4]:int(t[5]), t[6]:int(t[7])})

   critere = {
      'children': 3,
      'cats': 7, 
      'samoyeds': 2,
      'pomeranians': 3,
      'akitas': 0,
      'vizslas': 0,
      'goldfish': 5,
      'trees': 3,
      'cars': 2,
      'perfumes': 1
   }
   
   print("Partie 1 : ", part1(lignes, critere))
   print("Partie 2 : ", part2(lignes, critere))


