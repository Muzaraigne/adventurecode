# -*- coding: utf-8 -*- 



from calendar import c


def find_combinations(capacities, target_volume, index, current_volume,current_combo):
   sol = []
   if current_volume > target_volume:
        return []
   if index == len(capacities):
        if current_volume == target_volume:
            return [current_combo]
        else:
            return []
   count_with_current = find_combinations(capacities,target_volume,index + 1,current_volume + capacities[index],current_combo + [capacities[index]])
   count_without_current = find_combinations(capacities,target_volume,index + 1,current_volume,current_combo)
   sol.extend(count_with_current)
   sol.extend(count_without_current)
   return sol


def solve_day17(capacities, target_volume):

    all_solutions = find_combinations(capacities, target_volume, 0, 0, [])
    part1_result = len(all_solutions)
    print(f"Partie 1: Le nombre de combinaisons pour atteindre un volume de {target_volume} est : {part1_result}")
    if not all_solutions:
        print("Partie 2: Aucune solution trouvée, donc pas de solution minimale.")
        return
    min_containers = min(len(solution) for solution in all_solutions)
    part2_result = sum(1 for solution in all_solutions if len(solution) == min_containers)
    print(f"Partie 2: Le nombre minimum de conteneurs est de {min_containers}.")
    print(f"Partie 2: Le nombre de combinaisons avec ce minimum de conteneurs est : {part2_result}")


if __name__ == "__main__" : 
   print("--- jour 17 : Non trop de choses comme trop (Solution) ---") 
   with open("2015/jour17/input.txt") as fichier :
      lignes = fichier.readlines()
      contenances = [int(ligne.strip()) for ligne in lignes]

   result = solve_day17(contenances, 150)