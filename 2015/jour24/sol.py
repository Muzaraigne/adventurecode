import itertools
import math

def ind_sums(liste, somme) :
    """ Renvoie les indices des éléments de liste dont la somme vaut somme """
    n = len(liste)
    for r in range(1, n+1) :
      for comb in itertools.combinations(range(n), r) :
        if sum(liste[i] for i in comb) == somme :
            yield comb

def resolve(l_colis,repartitions):
    total = sum(l_colis)
    cible = total // repartitions
    solutions_qe = []
    for r in range(1, len(l_colis) + 1):
        for indices1 in itertools.combinations(range(len(l_colis)), r):
            if sum(l_colis[i] for i in indices1) == cible:
                reste_indices = [i for i in range(len(l_colis)) if i not in indices1]
                reste = [l_colis[i] for i in reste_indices]
                groupe2_existe = any(1 for _ in ind_sums(reste, cible))
                if groupe2_existe:
                    qe = math.prod(l_colis[i] for i in indices1)
                    solutions_qe.append(qe)       
        if solutions_qe:
            return min(solutions_qe)

    return None

if __name__ == "__main__":
    print("--- Jour 24 : Soluce ---")
    with open("2015/jour24/input.txt") as f:
        lignes = f.read().split("\n")
    l_colis = [int(li) for li in lignes if li]
    
    print("Partie 1 :", resolve(l_colis, 3))
    print("Partie 2 :", resolve(l_colis, 4))