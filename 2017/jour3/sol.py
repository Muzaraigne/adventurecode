# -*- coding: utf-8 -*- 

import math

def calculer_distance_spirale(data: int) -> int:
    """
    Calcule la distance de Manhattan du nombre 'data' au centre (1) d'une grille spirale.
    """
    if data == 1:
        return 0
    S = math.ceil(math.sqrt(data))
    if S % 2 == 0:
        S += 1
    R = (S - 1) // 2 
    max_val = S * S
    longueur_cote = S - 1
    difference = max_val - data
    position_sur_cote = (difference % longueur_cote)
    offset = abs(position_sur_cote - R)
    
    
    return R+offset

def calculer_somme_spirale(data_InDATA_INPUT: int) -> int:
  """
  Calcule la première valeur dans la spirale de somme des voisins
  qui est supérieure à data_InDATA_INPUT (Partie 2).
  """
  grid = {(0, 0): 1}
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  x, y = 0, 0
  dir_index = 0
  segment_length = 1
  steps_taken = 0
  turns = 0
  while True:
    dx, dy = directions[dir_index]
    x += dx
    y += dy
    steps_taken += 1
    nouvelle_valeur = get_sum_of_neighbors(x, y,grid)
    grid[(x, y)] = nouvelle_valeur
    if nouvelle_valeur > data_InDATA_INPUT:
      return nouvelle_valeur
    if steps_taken == segment_length:
      steps_taken = 0
      dir_index = (dir_index + 1) % 4
      turns += 1      
      if turns % 2 == 0:
        segment_length += 1

def get_sum_of_neighbors(cx, cy,grid):
  """Calcule la somme des 8 voisins (déjà remplis) de (cx, cy)."""
  somme = 0
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if dx == 0 and dy == 0:
        continue  
      voisin = (cx + dx, cy + dy)
      if voisin in grid:
        somme += grid[voisin]
  return somme




if __name__ == "__main__":
    DATA_INPUT = 289326
    print("--- Jour 3 : Calcul de la Distance Spirale ---")
    print(f"Distance pour 1: {calculer_distance_spirale(1)}")      
    print(f"Distance pour 12: {calculer_distance_spirale(12)}")  
    print(f"Distance pour 10: {calculer_distance_spirale(10)}")   
    print(f"Distance pour 1024: {calculer_distance_spirale(1024)}")
    print("-" * 35)
    resultat = calculer_distance_spirale(DATA_INPUT)
    print(f"Distance pour {DATA_INPUT}: {resultat}")

   
    print("--- Jour 3 Partie 2 : Spirale de Somme des Voisins ---")
    print(f"L'entrée cible est : {DATA_INPUT}")

    
    print(f"La première valeur supérieure à 1: {calculer_somme_spirale(1)}")    # 2
    print(f"La première valeur supérieure à 25: {calculer_somme_spirale(25)}") # 26

    resultat_partie_2 = calculer_somme_spirale(DATA_INPUT)
    print(f"La première valeur générée supérieure à {DATA_INPUT} est : {resultat_partie_2}")
