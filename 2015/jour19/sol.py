# -*- coding: utf-8 -*- 
import re
def solve_day19_part1(input_data):


    molecule = lines[-1]

    rules = {}
    for line in lines[:-2]:
        source, replacement = line.split(" => ")
        if source not in rules:
            rules[source] = []
        rules[source].append(replacement)

    unique_molecules = set()

    for source, replacements in rules.items():
        start_index = molecule.find(source, 0)
        while start_index != -1 :

            
            # Pour chaque remplacement possible pour cette source
            for replacement in replacements:
                # Construire la nouvelle molécule
                new_molecule = molecule[:start_index] + replacement + molecule[start_index + len(source):]
                unique_molecules.add(new_molecule)
            
            # Continuer la recherche après l'index trouvé
            start_index = molecule.find(source, start_index+1)
            
    return len(unique_molecules)

def solve_day19_part2(input_data):
    """
    Résout la deuxième partie de l'énigme du jour 19.

    Trouve le nombre minimal d'étapes pour réduire la molécule de départ à 'e'.
    """

    molecule = lines[-1]
    atoms = re.findall(r'[A-Z][a-z]*', molecule)
    num_atoms = len(atoms)
    num_rn = molecule.count("Rn")
    num_ar = molecule.count("Ar")
    num_y = molecule.count("Y")
    steps = num_atoms - num_rn - num_ar - (2 * num_y) - 1
            
    return steps


if __name__ == "__main__" : 
   print("--- Jour 19 Médecine pour Rudolph (Solution) ---")

   with open("2015/jour19/input.txt") as fichier :
      lines = fichier.read().strip().split('\n')
      result = solve_day19_part1(lines)
      print(f"Le nombre de molécules distinctes est : {result}")
      result = solve_day19_part2(lines)
      print(f"Le nombre minimal d'étapes pour réduire la molécule est : {result}")
      