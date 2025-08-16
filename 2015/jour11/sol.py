# -*- coding: utf-8 -*- 


def contient_sequence_croissante(mot):
    """
    Vérifie si un mot contient une séquence de trois lettres consécutives
    et croissantes de l'alphabet (comme 'abc', 'bcd', 'cde', etc.).
    """
    # On parcourt le mot jusqu'à l'avant-avant-dernière lettre pour pouvoir
    # vérifier les trois prochaines.
    for i in range(len(mot) - 2):
        # On extrait la sous-chaîne de trois lettres
        substring = mot[i:i+3]

        # On vérifie si la deuxième lettre est la suivante de la première,
        # et si la troisième est la suivante de la deuxième, en se basant sur leur
        # code numérique (ASCII).
        if ord(substring[1]) == ord(substring[0]) + 1 and \
           ord(substring[2]) == ord(substring[1]) + 1:
            return True
    
    # Si la boucle se termine sans trouver de séquence, on renvoie False
    return False


def had_truble_lettres(word:str):
   return 'o' in word or 'i' in word or 'l' in word



def haveDoubleDoubleLetters(chaine):
   for i in range(len(chaine) - 1):
        if chaine[i] == chaine[i + 1]:
            # Une première paire est trouvée.
            # On recherche une deuxième paire non chevauchante.
            for j in range(i + 2, len(chaine) - 1):
                if chaine[j] == chaine[j + 1]:
                    return True
   return False

def incrementer_mot_de_passe(mot_de_passe):
    mdp_list = list(mot_de_passe)
    for i in range(len(mdp_list) - 1, -1, -1):
        if mdp_list[i] == 'z':
            mdp_list[i] = 'a'
        else:
            mdp_list[i] = chr(ord(mdp_list[i]) + 1)
            return "".join(mdp_list)

    return "a".join(mdp_list)

def genMDP(oldMpd):
    newMdp = incrementer_mot_de_passe(oldMpd)
    
    while not( not had_truble_lettres(newMdp) and \
           haveDoubleDoubleLetters(newMdp) and \
           contient_sequence_croissante(newMdp)):
        newMdp = incrementer_mot_de_passe(newMdp)

    return newMdp

if __name__ == "__main__" : 
    print("Jour 11 Advent of Code 2015")

    mdp = "hxbxwxba"
    nouveau_mdp = genMDP(mdp)
    print(f"Le mot de passe suivant est : {nouveau_mdp}")
    print(f"le mot de passe d'après  est {genMDP(nouveau_mdp)} ")