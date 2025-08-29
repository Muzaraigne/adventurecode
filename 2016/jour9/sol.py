# -*- coding: utf-8 -*- 



import re


def decompressed_rapide(chaine):
    """
    Décompresse une chaîne de caractères en utilisant une approche basée sur une liste
    pour une meilleure performance.
    """
    parties = []
    i = 0
    while i < len(chaine):
        if chaine[i] == '(':

            correspondance = re.match(r'\((\d+)x(\d+)\)', chaine[i:])
            if correspondance:
                longueur, repetition = int(correspondance.group(1)), int(correspondance.group(2))
                longueur_marqueur = len(correspondance.group(0))
                debut_donnees = i + longueur_marqueur
                fin_donnees = debut_donnees + longueur
                if fin_donnees > len(chaine):
                    parties.append(chaine[i:])
                    break
                
                a_repeter = chaine[debut_donnees:fin_donnees]
                parties.append(a_repeter * repetition)
                i = fin_donnees
                continue
        
        parties.append(chaine[i])
        i += 1
        
    return "".join(parties)


def calculate_decompressed_length(chaine):
    length = 0
    i = 0
    while i < len(chaine):
        if chaine[i] == '(':
            match = re.search(r'\((\d+)x(\d+)\)', chaine[i:])
            if match:
                marker_length = len(match.group(0))
                sub_length = int(match.group(1))
                repetitions = int(match.group(2))
                sub_string = chaine[i + marker_length : i + marker_length + sub_length]
                decompressed_sub_length = calculate_decompressed_length(sub_string)
                length += decompressed_sub_length * repetitions
                i += marker_length + sub_length
                continue
        length += 1
        i += 1
        
    return length

if __name__ == "__main__" : 
    print("--- Jour 9 : Solution ---") 
    with open(".\\2016\\jour9\\input.txt","r") as f : 
       data = f.read().splitlines() 

    data_test = [
        'ADVENT',
        'A(1x5)BC',
        '(3x3)XYZ',
        'A(2x2)BCD(2x2)EFG',
        '(6x1)(1x3)A',
        'X(8x2)(3x3)ABCY'
    ]
    reponse_test = [
        'ADVENT',
        'ABBBBBC',
        'XYZXYZXYZ',
        'ABCBCDEFEFG',
        '(1x3)A',
        'X(3x3)ABC(3x3)ABCY'
    ]

    for i in range(len(data_test)):
        f =  decompressed_rapide(data_test[i])
        if f == reponse_test[i]:
            print('no problem')
        else : 
            print('error, attend',reponse_test[i],'optain ',f)


    print("Partie 1 : ")
    print("lachaine compréssé fait :",len(data[0]),"caractères")
    print("la nouvelle chaine decompressee a une longueur de ",len(decompressed_rapide(data[0])),"caractères")
    print("Partie 2 :")
    print("Avec la nouvelle methode la chaine va faire ",calculate_decompressed_length(data[0]),"caractères")