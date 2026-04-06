# -*- coding: utf-8 -*- 


def marche(data,time):
    incr = 1
    for d in data : 
        mod,dep =d
        if (dep+time+incr)%mod> 0:
            return False
        incr += 1
        
    return True


def calcul(data):
    
    time = 0 
    while True:
        if marche(data,time) :
            return time 
        time += 1
   
if __name__ == "__main__" : 
    print("--- Jour 15 : Solution ---") 
    data = [
        (17,15),
        (3,2),
        (19,4),
        (13,2),
        (7,2),
        (5,0),
    ]

    data_test = [
        (5,4),
        (2,1)
    ]

    print("Le data set de test donne sur mon algorythme : ",calcul(data_test))
    print("Partie 1 : Il faut presser le bouton a ",calcul(data)," time")
    data.append((11,0))
    print("Partie 2 : Avec l'ajout du nouveau disque , on a le boutton a presser a  ",calcul(data)," time")
