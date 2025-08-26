# -*- coding: utf-8 -*- 
import re


def valid_triangles(sides) : 
    a,b,c = sorted(sides) 
    return a+b>c

def soluce_part1(data) : 
    count = 0 
    for line in data : 
        sides = [int(x) for x in line.split()]
        if valid_triangles(sides) : 
            count += 1 
    return count


def soluce_part2(data) : 
    count = 0 
    for i in range(0,len(data),3) : 
        sides1 = [int(x) for x in data[i].split()]
        sides2 = [int(x) for x in data[i+1].split()]
        sides3 = [int(x) for x in data[i+2].split()]
        for j in range(3) : 
            sides = [sides1[j],sides2[j],sides3[j]]
            if valid_triangles(sides) : 
                count += 1
    return count

if __name__ == "__main__" : 
    print("--- Jour 3 : Solution ---") 
    with open(".\\2016\\jour3\\input.txt","r") as f : 
       data = f.read().splitlines() 
    print("Partie 1 : Il y a  ",soluce_part1(data)," triangles valides")
    print("Partie 2 : Il y a  ",soluce_part2(data)," triangles valides")