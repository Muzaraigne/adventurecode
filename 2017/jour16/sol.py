# -*- coding: utf-8 -*-


def spin(n,li):
    return li[-n:] + li[:-n]
    
def exchange(n1,n2,l):
  l[n1], l[n2] = l[n2], l[n1]
  
def partener(v1,v2,l):
  for i in range(len(l)):
     if l[i] == v1 : 
        l[i] = v2
     elif l[i] == v2 :
        l[i] = v1
      
def sim(data,prog ):
   res = prog.copy()
   for d in data :
      if d[0] == 's' :
        res = spin(int(d[1:]),res)
      elif d[0] == 'x':
         parts = d[1:].split('/')
         exchange(int(parts[0]),int(parts[1]),res)
      elif d[0] == 'p':
         parts = d[1:].split('/')
         partener(parts[0],parts[1],res)
      else : 
         continue
   return "".join(res)

def repeat(n, data, prog):
   seen = {}
   tmp = prog
   for i in range(n):
       state = "".join(tmp)
       if state in seen:
           # Found a cycle
           cycle_start = seen[state]
           cycle_length = i - cycle_start
           remaining = (n - cycle_start) % cycle_length
           # Run remaining iterations
           for _ in range(remaining):
               result = sim(data, tmp)
               tmp = list(result)
           return "".join(tmp)
       seen[state] = i
       result = sim(data, tmp)
       tmp = list(result)
   return "".join(tmp)
   
if __name__ == "__main__" : 
  print("--- Jour 16 : Solution ---") 
  with open(".\\2017\\jour16\\input.txt","r") as f : 
       data = f.read().strip().split(',') 
  data_test = "s1,x3/4,pe/b".split(',')
  prog_test = [chr(i) for i in range(ord("a"), ord("e") + 1)]
  prog = [chr(i) for i in range(ord("a"), ord("p") + 1)]

  print("-----Test-----")
  result = sim(data_test,prog_test)
  print(f"{result}")

  print("-----Partie1-----")
  print(f"la séquence a la fin de la danse est {sim(data,prog)}")
  print("-----Partie2-----")
  print(f"la séquence a la fin de la danse est {repeat(1000000000,data,prog)}")