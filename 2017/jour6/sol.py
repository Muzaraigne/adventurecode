# -*- coding: utf-8 -*- 
from numpy import index_exp


def max_ind(li): 
    """
    Trouve l'indice de la première occurrence de la valeur maximale.
    Optimisé en utilisant max() avec enumerate.
    """
    return max(enumerate(li), key=lambda item: item[1])[0]


def spread(liste) :
  """
    Distribue la valeur maximale aux banques suivantes de manière cyclique.
    Correction : assure le démarrage à l'indice suivant (ind_m + 1).
  """
  ind_m = max_ind(liste)
  vm = liste[ind_m]
  size = len(liste)
  liste[ind_m] = 0
  start_index = ind_m + 1
  for i in range(vm):
        idx = (start_index + i) % size
        liste[idx] += 1

def destribution(data) : 
    seen_states = list()
    cycles = 0
    current_state = tuple(data.copy()) 

    while current_state not in seen_states:
        seen_states.append(current_state)
        spread(data)
        current_state = tuple(data.copy())  
        cycles += 1

    return (cycles,seen_states.index(current_state))

def test():
   banks = [0,2,7,0]
   resc,resp = destribution(banks)
   if resc != 5 :
      print(f'error: we expeted : 5 and we got {resc}')
   dif = resc-resp
   if dif !=4 : 
       print(f'error: we expeted : 4 and we got {dif}')
    
if __name__ == "__main__" : 
  print("--- Jour 6 : Solution ---") 
  with open(".\\2017\\jour6\\input.txt","r") as f : 
    data = f.read().splitlines()[0]
    banks = [int(x) for x in data.split()] 
  test()
  cycles,prem = destribution(banks)
  print(f'Il faut {cycles}, la premiere fois qu\'on le trouve c\'est à la {prem} repartition donc une distance de {cycles-prem}')
