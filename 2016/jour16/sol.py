# -*- coding: utf-8 -*- 
def courbe_dragon_inverse(data: str): 
    return data + '0'+ ''.join('1' if c == '0' else '0' for c in data[::-1])

def control_sum(info):
    while len(info) % 2 == 0:
        info = ''.join(
            '1' if info[i] == info[i+1] else '0'
            for i in range(0, len(info), 2)
        )
    return info


def sol_part(data,long):
    crypt = data
    while len(crypt) < long :
        crypt = courbe_dragon_inverse(crypt)
    return control_sum(crypt[:long])

if __name__ == "__main__" : 
    print("--- Jour 16 : Solution ---") 
    data = '01000100010010111'
    longueur =272
    long_par2 =35651584

    print("Partie de test : ")
    print("test de la courbe du dragon inversé: ")
    print(courbe_dragon_inverse('0') == '001')
    print(courbe_dragon_inverse('1') == '100')
    print(courbe_dragon_inverse('11111') == '11111000000')
    print(courbe_dragon_inverse('111100001010') == '1111000010100101011110000')
    print('test de la somme de controle : ')
    print(control_sum('110010110100') == '100')
    print("test du total : ")
    print(sol_part('10000',20) == '01100')

    print("Part 1 : La somme de controle pour le premier disque est ", sol_part(data,longueur))
    print("Part 2 : La somme de controle pour le deuxieme disque est ",sol_part(data,long_par2))

    
