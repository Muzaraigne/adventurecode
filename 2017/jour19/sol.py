# -*- coding: utf-8 -*-

def parcourt(data):
    res = ""
    j = 0
    i = data[0].index('|') if '|' in data[0] else 0
    dj, di = 1, 0  
    steps = 0
    
    while True:
        j += dj
        i += di
        steps += 1
        if j < 0 or j >= len(data) or i < 0 or i >= len(data[j]):
            break
        cell = data[j][i]
        if cell == ' ':
            break
        if cell.isalpha():
            res += cell
        if cell == '+':
            for new_dj, new_di in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (new_dj, new_di) == (-dj, -di):
                    continue
                nj, ni = j + new_dj, i + new_di
                if nj < 0 or nj >= len(data) or ni < 0 or ni >= len(data[nj]):
                    continue
                if data[nj][ni] != ' ':
                    dj, di = new_dj, new_di
                    break

    return res, steps

if __name__ == "__main__" : 
  print("--- Jour 19 : Solution ---") 
  with open(".\\2017\\jour19\\input.txt","r") as f : 
       data = [list(line.rstrip('\n')) for line in f.readlines()]

  print('-----Partie 1------')
  letters, steps = parcourt(data)
  print(f'La suite de lettres dans le labyrinthe : {letters}')
  print(f'Nombre de pas : {steps}')