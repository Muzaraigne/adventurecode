# -*- coding: utf-8 -*- 

def deplacement(c) : 
    if c == 'D' :
        return (0,1)
    elif c == 'U' :
        return (0,-1)
    elif c == 'L' :
        return (-1,0)
    elif c == 'R' :
        return (1,0)
    
def decode_digital(data) : 
    digital_pad = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    res = ""
    pos = (1,1)
    for line in data:
        for instruction in line:
            m = deplacement(instruction)
            new_pos = (pos[0] + m[0], pos[1] + m[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                pos = new_pos
        
       
        res += str(digital_pad[pos[1]][pos[0]])
        
    return res
def decode_weird(data) :
    weird_pad = [
        [None,None,1,None,None],
        [None,2,3,4,None],
        [5,6,7,8,9],
        [None,'A','B','C',None],
        [None,None,'D',None,None]
    ]
    res = ""
    pos = (0,2)
    for line in data:
        for instruction in line:
            m = deplacement(instruction)
            new_pos = (pos[0] + m[0], pos[1] + m[1])
            if 0 <= new_pos[0] < 5 and 0 <= new_pos[1] < 5 and weird_pad[new_pos[1]][new_pos[0]] is not None:
                pos = new_pos
        
       
        res += str(weird_pad[pos[1]][pos[0]])
        
    return res
if __name__ == "__main__" : 
    print("--- Jour 2 : Solution ---") 
    with open(".\\2016\jour2\input.txt","r") as f : 
       data = f.read().splitlines() 
    
    print("le code pour la salle de bain est :",decode_digital(data))
    print("le code pour la salle de bain bizarre est :",decode_weird(data))
