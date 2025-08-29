# -*- coding: utf-8 -*- 


import re

def standart_ins(instruction):
    # Modèle pour 'rect 3x2'
    match_rect = re.search(r'rect (\d+)x(\d+)', instruction)
    if match_rect:
        return {
            'type': 'rect',
            'row': int(match_rect.group(1)),
            'column': int(match_rect.group(2))
        }

    # Modèle pour 'rotate row y=0 by 4'
    match_row = re.search(r'rotate row y=(\d+) by (\d+)', instruction)
    if match_row:
        return {
            'type': 'row',
            'lieu': int(match_row.group(1)),
            'ecart': int(match_row.group(2))
        }

    # Modèle pour 'rotate column x=1 by 1'
    match_column = re.search(r'rotate column x=(\d+) by (\d+)', instruction)
    if match_column:
        return {
            'type': 'column',
            'lieu': int(match_column.group(1)),
            'ecart': int(match_column.group(2))
        }
    
    return None

def print_ec(ecran):
    for i in ecran :
        print(i)

def rect (ecran,instruction):
    row = instruction['row']
    column =instruction['column']
    for i in range(column):
        for j in range(row):
            ecran[i][j] = '#'

def rotate_column(ecran,instruction):
    endroit = instruction['lieu']
    ecart = instruction['ecart']
    nombre_lignes = len(ecran)
    colonne_temp = [ecran[i][endroit] for i in range(nombre_lignes)]
    for i in range(nombre_lignes):
        nouvel_index = (i + ecart) % nombre_lignes
        ecran[nouvel_index][endroit] = colonne_temp[i]
    
def rotate_row(ecran,instruction):
    endroit = instruction['lieu']
    ecart = instruction['ecart']
    longueur_ligne = len(ecran[endroit])
    ligne_temp = ecran[endroit].copy()

    for i in range(longueur_ligne):
        nouvel_index = (i + ecart) % longueur_ligne
        ecran[endroit][nouvel_index] = ligne_temp[i]


def process_instruction(ecran,instruction):
    """
    process the instruction put in parameter
    """
    inst = standart_ins(instruction)
    if inst['type'] == 'rect':
        rect(ecran,inst)
    else:
        if inst['type'] =='row' :
            rotate_row(ecran,inst)
        elif inst['type'] == 'column':
            rotate_column(ecran,inst)
    return ecran    
    
def count_on (data) :
   return sum([ligne.count('#') for ligne in data])

def sol_part1(inst):
    ec = [['.' for j in range(50)] for i in range(6)]
    for i in inst :
        process_instruction(ec,i)
    return ec


    
if __name__ == "__main__" : 
    print("--- Jour 8 : Solution ---") 
    with open(".\\2016\\jour8\\input.txt","r") as f : 
        data = f.read().splitlines() 

    ecran_test = [
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.']
    ]
    instruction =[
        'rect 3x2',
        'rotate column x=1 by 1',
        'rotate row y=0 by 4',
        'rotate column x=1 by 1'
    ]
    for i in instruction :
        process_instruction(ecran_test,i)

    print("process des instructions de l'exempleet voici l'affichge de l'ecran")
    print_ec(ecran_test)

    res = sol_part1(data)
    print("Partie 1 :")
    print("Il y a ",count_on(res)," pixels allumés")
    print('Partie 2 :')
    print("il vous suffit donc de lire le message,il faut avoir un ecran assez grand (pas trouver mieux ^^)")
    print_ec(res)

    