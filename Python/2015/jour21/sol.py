# -*- coding: utf-8 -*- 
import json
import itertools

def fight(player, boss):
   player_damage = max(1, player['damage'] - boss['armor'])
   boss_damage = max(1, boss['damage'] - player['armor'])
   player_hp = player['hp']
   boss_hp = boss['hp']
   while True:
      boss_hp -= player_damage
      if boss_hp <= 0:
         return True # Le joueur gagne
   
      player_hp -= boss_damage
      if player_hp <= 0:
         return False # Le boss gagne

def sol_part1(boss, weapons, armors, rings, base_stats):
   min_cost = float('inf')
   for weapon in weapons:
      for armor in armors:
         for i in range(len(rings)):
            for j in range(i, len(rings)):
            
               # Créer une copie des statistiques de base
               my_stats = base_stats.copy()
            
               total_cost = weapon['cost'] + armor['cost'] + rings[i]['cost'] + rings[j]['cost']
               my_stats['damage'] += weapon['damage'] + rings[i]['damage'] + rings[j]['damage']
               my_stats['armor'] += armor['armor'] + rings[i]['armor'] + rings[j]['armor']
            
               if fight(my_stats, boss):
                  min_cost = min(min_cost, total_cost)
   return min_cost

def sol_part2(boss, weapons, armors, rings, base_stats):
   m = -1e100
   for i0 in weapons:
      for i1 in armors:
         for i2, i3 in itertools.combinations(rings, 2):
               php = 100
               cost = i0['cost'] + i1['cost'] + i2['cost'] + i3['cost']
               pdmg = i0['damage'] + i1['damage'] + i2['damage'] + i3['damage']
               parmr = i0['armor'] + i1['armor'] + i2['armor'] + i3['armor']
               player = {'hp': php, 'damage': pdmg, 'armor': parmr}
               if not fight(player, boss):
                  m = max(m, cost)
   return m
if __name__ == "__main__" : 
   print("--- Jour 21: Soluce ---") 
   with open('2015/jour21/input.json', 'r') as f:
      data = json.load(f)
      weapons = data['weapons']
      armors = data['armors']
      rings = data['rings']
      my_stats = data['my_stats']
      boss = data['boss_stats']

   # Assurez-vous d'avoir les bonnes stats pour le boss dans votre input.json
   print("boss stats : ", boss)
   print("Partie 1 : Le cout minimum pour gagner est de ", sol_part1(boss, weapons, armors, rings, my_stats))
   print("Partie 2 : Le cout maximum pour perdre est de ", sol_part2(boss, weapons, armors, rings, my_stats))