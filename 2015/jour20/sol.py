# -*- coding: utf-8 -*- 
def solve_elf_problem(objectif, cadeaux_par_elfe, maisons_visitees=None):
    max_maison = objectif // cadeaux_par_elfe
    houses = [0] * (max_maison * 2) 

    
    for elfe in range(1, len(houses)):
        if maisons_visitees is not None:
            
            for i in range(1, maisons_visitees + 1):
                maison = elfe * i
                if maison >= len(houses):
                    break
                houses[maison] += elfe * cadeaux_par_elfe
        else:
            
            for maison in range(elfe, len(houses), elfe):
                houses[maison] += elfe * cadeaux_par_elfe

    
    for k in range(1, len(houses)):
        if houses[k] >= objectif:
            return k
    
    return -1


if __name__ == "__main__":
    print("--- Jour 20 : Elfes infinis et maisons infinies (Solution) ---")
    try:
        objectif = int(input("Entrez l'objectif : "))
        if objectif <= 0:
            print("L'objectif doit être un entier positif.")
            exit(1)

        #result_p1 = solve_elf_problem(objectif, 10)
       #print(f"Pour la partie 1, la maison est : {result_p1}")

        result_p2 = solve_elf_problem(objectif, 11, 50)
        print(f"Pour la partie 2, la maison est : {result_p2}")

    except ValueError:
        print("L'objectif doit être un entier.")
        exit(1)
