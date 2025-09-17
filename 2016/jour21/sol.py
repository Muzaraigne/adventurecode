# -*- coding: utf-8 -*- 

from itertools import chain
from re import split


def swap_pos(chaine,x,y):
    chaine = list(chaine)
    cx = chaine[x]
    chaine[x]=chaine[y]
    chaine[y] = cx
    return ''.join(chaine)

def swap_letter(chaine,c1,c2):
    chaine = list(chaine)
    for i in range(len(chaine)) :
        c = chaine[i]
        if c == c1 :
            chaine[i] = c2
        if c == c2 :
            chaine[i] =c1
    return ''.join(chaine)

def rotate(chaine,n):
    # left = n positif / right = n négatif
    chaine = list(chaine)
    chaine = chaine[n:] + chaine[:n]
    return ''.join(chaine)

def rotate_letter(chaine,x):
    ind = chaine.index(x)
    rotation_steps = -(1 + ind)
    chaine = rotate(chaine, rotation_steps)
    if ind >= 4:
        chaine = rotate(chaine, -1)  
    return chaine


def move(chaine,x,y):
    char_list = list(chaine)
    char_to_move = char_list.pop(x)
    char_list.insert(y, char_to_move)
    return "".join(char_list)

def reverse (chaine,x,y):
    ch = list(chaine)
    sublist_to_reverse = ch[x:y+1]
    reversed_sublist = sublist_to_reverse[::-1]
    ch[x:y+1] = reversed_sublist
    return ''.join(ch)

def apply(data,chaine):
    d = data.split(' ')
    if 'swap' in data :
        if 'position' in data :
            return swap_pos(chaine,int(d[2]),int(d[len(d)-1]))
        else : 
            return swap_letter(chaine,d[2],d[len(d)-1])
    elif 'move ' in data :
        return move(chaine,int(d[2]),int(d[len(d)-1]))
    elif 'rotate' in data:
        if 'left' in data : 
            return rotate(chaine,int(d[len(d)-2]))
        elif 'right' in data :
            return rotate(chaine,-int(d[len(d)-2]))
        else :
            return rotate_letter(chaine,d[len(d)-1])
    elif 'reverse' in data: 
        return reverse(chaine,int(d[2]),int(d[len(d)-1]))
    pass

def compute(data,input):
    chaine = input
    for d in data : 
        chaine = apply(d,chaine)
    return chaine

def test(data,sol):
    scrambling_test= 'abcde'
    er =0
    for i in range(len(data)):
        scrambling_test=apply(data[i],scrambling_test)
        if scrambling_test != sol[i] :
            er +=1
            print(f'error {er}, attend : {sol[i]} , we got {scrambling_test}')
        else : 
            print('test passed' )
    pass
def inverse_rotate_letter(chaine, x):
    for i in range(len(chaine)):
        candidate = rotate(chaine, i)
        if rotate_letter(candidate, x) == chaine:
            return candidate
    raise ValueError("Pas trouvé")
def apply_inverse(data, chaine):
    d = data.split(' ')
    if 'swap' in data:
        if 'position' in data:
            return swap_pos(chaine, int(d[2]), int(d[-1]))
        else:
            return swap_letter(chaine, d[2], d[-1])
    elif 'move' in data:
        return move(chaine, int(d[-1]), int(d[2]))  # inversion
    elif 'rotate' in data:
        if 'left' in data:
            return rotate(chaine, -int(d[-2]))
        elif 'right' in data:
            return rotate(chaine, int(d[-2]))
        else:
            return inverse_rotate_letter(chaine, d[-1])
    elif 'reverse' in data:
        return reverse(chaine, int(d[2]), int(d[-1]))
def compute_inverse(data, input):
    chaine = input
    for d in data[::-1]: 
        chaine = apply_inverse(d, chaine)
    return chaine

if __name__ == "__main__" : 
    print("--- Jour 21 : Solution ---") 
    with open(".\\2016\\jour21\\input.txt","r") as f : 
       data = f.read().splitlines() 
    scrambling = 'abcdefgh'

    data_test = [
        'swap position 4 with position 0',
        'swap letter d with letter b',
        'reverse positions 0 through 4',
        'rotate left 1 step',
        'move position 1 to position 4',
        'move position 3 to position 0',
        'rotate based on position of letter b',
        'rotate based on position of letter d'
    ]
    
    sol_test = [
        'ebcda',
        'edcba',
        'abcde',
        'bcdea',
        'bdeac',
        'abdec',
        'ecabd',
        'decab'
    ]
    test(data_test,sol_test)
    print(f'Partie 1 : Le mot de passe brouillé est {compute(data,scrambling)}')
    print(f'Partie 2 : le mot de passe désbrouiller est {compute_inverse(data,'fbgdceah')}')
    
