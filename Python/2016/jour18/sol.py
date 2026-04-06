# -*- coding: utf-8 -*- 
def its_trap(g,d):
    return '^' if g != d else '.'

def generate_row(row):
    res = ''
    res += its_trap('.',row[1])
    for i in range(1,len(row)-1):
        res += its_trap(row[i-1],row[i+1])
    res += its_trap(row[-2],'.')
    return res

def generate_salle(entry,leng):
    res = [entry]
    for i in range(1,leng):
        res.append(generate_row(res[i-1]))
    return res

def count_safe(salle):
    return sum([
        i.count('.') for i in salle
    ])

def test():
    data = [
        '..^^.',
        '.^^^^',
        '^^..^'
    ]

    return generate_salle(data[0],len(data)) == data

def test2():
    data = [
        '^^^...^..^',
        '^.^^.^.^^.',
        '..^^...^^^',
        '.^^^^.^^.^',
        '^^..^.^^..',
        '^^^^..^^^.',
        '^..^^^^.^^',
        '.^^^..^.^^',
        '^^.^^^..^^'
    ]
    return generate_salle(data[0],len(data)) == data
if __name__ == "__main__" : 
    print("--- Jour 18 : Solution ---") 
    with open(".\\2016\\jour18\\input.txt","r") as f : 
       data = f.read().splitlines() 
       row = data[0]
       nb = int(data[1])
       nb2= int(data[2])

    if not test() :
        print('le premier test en passe pas ')
    if not test2() : 
        print('le deuxieme test ne passe pas ')

    print("Partie 1 : il y a ",count_safe(generate_salle(row,nb))," carreau sûr")
    print("Partie 2 : il y a ",count_safe(generate_salle(row,nb2))," carreau sûr")