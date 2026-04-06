# -*- coding: utf-8 -*- 
dir = {
        "ne":(+1,+1),
        "sw" : (-1,-1),
        "se":(+1,0),
        "nw":(-1,0),
        "n":(0,1),
        "s":(0,-1)
}
def minpas(data):
    pos= (0,0)
    for d in data : 
        p = dir[d]
        pos = (pos[0]+p[0],pos[1]+p[1])
    
    return max(abs(pos[0]),abs(pos[1]))

def maxpas(data):
    m = 0
    pos= (0,0)
    for d in data : 
        p = dir[d]
        pos = (pos[0]+p[0],pos[1]+p[1])
        m = max(m,max(abs(pos[0]),abs(pos[1])))    
    return m

def test():
    data_test = [
        ('ne,ne,ne',3),
        ('ne,ne,sw,sw',0),
        ('ne,ne,s,s',2),
        ('se,sw,se,sw,sw',3)
    ]  
    for d,v in data_test:
        rep = minpas(d.split(',')) 
        if  rep != v : 
            print(f'error test : for {d} we got {rep} we expected {v}')
    


if __name__ == "__main__" : 
  print("--- Jour 11 : Solution ---") 
  with open(".\\2017\\jour11\\input.txt","r") as f : 
       data = f.read().split(',')
  test()
  print(f'Partie 1 : Le nombre minimum de pas est de {minpas(data)}')
  print(f'Partie 2 : Le nombre maximum de pas est de {maxpas(data)}')
