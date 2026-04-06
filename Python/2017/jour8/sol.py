# -*- coding: utf-8 -*- 


def transform(li): 
   val1 , comp, val2 = li
   if comp == '>' : 
      return val1 > val2
   elif comp == '<' : 
      return val1 < val2
   elif comp == '>=' : 
      return val1 >= val2
   elif comp == '<=' : 
      return val1 <= val2
   elif comp == '==' : 
      return val1 == val2
   elif comp == '!=' : 
      return val1 != val2
   else : 
      return None
   

def compute(data):
   register = dict() 
   max_all = 0 
   for d in data : 
      d = d.split(' ')
      if not register.get(d[0]) :
        register[d[0]] = 0
      if not register.get(d[4]) : 
         register[d[4]] =0
      li = (register[d[4]],d[5],int(d[6]))
      if transform(li) : 
         if d[1] == 'inc':
            register[d[0]] += int(d[2])
            if max_all < register[d[0]] :
               max_all =register[d[0]]
         elif d[1] == 'dec' :
            register[d[0]] -= int(d[2])
            if max_all < register[d[0]] :
               max_all =register[d[0]]
   return (register[max(register,key= register.get)],max_all)            

def test():
   data = ['b inc 5 if a > 1',
           'a inc 1 if b < 5',
           'c dec -10 if a >= 1',
           'c inc -20 if c == 10']
   reg = compute(data)
   print (reg)
   

if __name__ == "__main__" : 
  print("--- Jour 8 : Solution ---") 
  with open(".\\2017\\jour8\\input.txt","r") as f : 
      data = f.read().splitlines() 
  test()
  reg = compute(data)
  print(f'Partie 1 : La plus valeur est {reg[0]}')
  print(f'Partie 2 : La plus grande valeur jamais atteinte est {reg[1]}')