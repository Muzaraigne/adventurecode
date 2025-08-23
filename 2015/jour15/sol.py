# -*- coding: utf-8 -*- 
import json


def calculs_part1(data) :
   meuilleure_combinaison = 0
   for i in range(101) :
      for j in range(101-i) :
         for k in range(101-i-j) :
            x = 100 - i - j - k
            score = 1
            for prop in ['capacity','durability','flavor','texture'] :
               somme = i*data["Sugar"][prop] + j*data["Sprinkles"][prop] + k*data["Candy"][prop] + x*data["Chocolate"][prop]
               if somme < 0 : 
                  score = 0
                  break
               score *= somme
            if score > meuilleure_combinaison :
               meuilleure_combinaison = score
   return meuilleure_combinaison
   
def calculs_part2(data) :
   meuilleure_combinaison = 0
   for i in range(101) :
      for j in range(101-i) :
         for k in range(101-i-j) :
            x = 100 - i - j - k
            calories = i*data["Sugar"]['calories'] + j*data["Sprinkles"]['calories'] + k*data["Candy"]['calories'] + x*data["Chocolate"]['calories']
            if calories != 500 : 
               continue
            score = 1
            for prop in ['capacity','durability','flavor','texture'] :
               somme = i*data["Sugar"][prop] + j*data["Sprinkles"][prop] + k*data["Candy"][prop] + x*data["Chocolate"][prop]
               if somme < 0 : 
                  score = 0
                  break
               score *= somme
            if score > meuilleure_combinaison :
               meuilleure_combinaison = score
   return meuilleure_combinaison

if __name__ == "__main__" : 
   with open('2015/jour15/input.json','r') as f :
      data = json.load(f)
   
   print("--- jour 15 : La science pour les gens affamés (Solution) ---")
   print("Partie 1 : Le score de la meilleure combinaison est de",calculs_part1(data))
   print("Partie 2 : Le score de la meilleure combinaison avec 500 calories est de",calculs_part2(data))