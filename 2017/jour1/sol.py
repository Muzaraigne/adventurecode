# -*- coding: utf-8 -*- 

def result(entry):
    """
    Résout le Captcha du Jour 1, Partie 1 (AoC 2017).
    Calcule la somme des chiffres qui correspondent au chiffre suivant dans la séquence, 
    en considérant que le dernier chiffre est suivi du premier.
    """
    # S'assure que l'entrée est une chaîne de caractères
    entry = str(entry)
    res = 0 
    
    # 1. Parcourt et vérifie les paires de chiffres adjacents
    # La boucle va de l'indice 0 jusqu'à l'avant-dernier indice (len(entry)-2)
    for i in range(0, len(entry) - 1):
        if entry[i] == entry[i+1]: 
            # Si les chiffres correspondent, ajoute la valeur du chiffre (entry[i]) au résultat
            res += int(entry[i])
            
    # 2. Vérifie la paire enveloppée (le dernier chiffre avec le premier)
    if entry[0] == entry[-1]:
        # Si le premier et le dernier correspondent, ajoute la valeur du premier chiffre
        res += int(entry[0])
        
    return res 

def result2 (entry): 
    entry = str(entry)
    moitie = round(len(entry)/2)
    res = 0
    for i in range(0,moitie):
        if entry[i] == entry[i+moitie] :
            res+= int(entry[i])*2
    return res
def test():
    a,b,c,d =result('1122'),result('1111'),result('1234'),result('91212129') 
    if not a==3:
        print(f'error: got:{a} expeted 3') 
    if not b == 4:
       print(f'error: got:{b} expeted 4') 
    if not c == 0:
       print(f'error: got:{c} expeted 0') 
    if not d == 9:
       print(f'error: got:{d} expeted 9') 

def test2():
    a,b,c,d,e =result2('1212'),result2('1221'),result2('123425'),result2('123123'), result2('12131415') 
    if not a==6:
        print(f'error: got:{a} expeted 6') 
    if not b == 0:
       print(f'error: got:{b} expeted 0') 
    if not c == 4:
       print(f'error: got:{c} expeted 4') 
    if not d == 12:
       print(f'error: got:{d} expeted 12') 
    if not e == 4 :
        print(f'error: got:{e} expeted 4') 

if __name__ == "__main__" : 
  print("--- Jour 1 : Solution ---") 
  with open(".\\2017\\jour1\\input.txt","r") as f : 
       data = f.read().strip()
  test()
  test2()
  print('Partie 1 : Le capcha vaut ',result(data))
  print('Partie 2 : Le capcha vaut ',result2(data))

