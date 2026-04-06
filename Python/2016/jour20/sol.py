# -*- coding: utf-8 -*- 

def toutes_les_ip_valides(intervals, max_ip):
    ranges = []
    for s in intervals:
        debut, fin = map(int, s.split("-"))
        ranges.append((debut, fin))

    ranges.sort(key=lambda x: x[0])

    current_min = 0
    valides = []

    for debut, fin in ranges:
        if debut > current_min:
            valides.extend(range(current_min, debut))
        if fin >= current_min:
            current_min = fin + 1


    if current_min <= max_ip:
        valides.extend(range(current_min, max_ip + 1))

    return valides


        
if __name__ == "__main__" : 
    print("--- Jour 20 : Solution ---") 
    with open(".\\2016\\jour20\\input.txt","r") as f : 
       data = f.read().splitlines() 
    max_ip = 4294967295
    data_test=["5-8","0-2","4-7"]

print("data test donne ", toutes_les_ip_valides(data_test,9))
print("Partie 1 : La plus petite adresse ip possible est :",toutes_les_ip_valides(data,max_ip)[0])
print("Partie 2 : Il y a ",len(toutes_les_ip_valides(data,max_ip)),"IP valide")
