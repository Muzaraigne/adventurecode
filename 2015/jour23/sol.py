# -*- coding: utf-8 -*- 

def calcule(data,registre) :
   i = 0
   while i < len(data) :
         inst = data[i].split()
         if inst[0] == "hlf" :
            registre[inst[1]] //= 2
            i += 1
         elif inst[0] == "tpl" :
            registre[inst[1]] *= 3
            i += 1
         elif inst[0] == "inc" :
            registre[inst[1]] += 1
            i += 1
         elif inst[0] == "jmp" :
            i += int(inst[1])
         elif inst[0] == "jie" :
            if registre[inst[1][:-1]] % 2 == 0 :
               i += int(inst[2])
            else :
               i += 1
         elif inst[0] == "jio" :
            if registre[inst[1][:-1]] == 1 :
               i += int(inst[2])
            else :
               i += 1
   return registre

if __name__ == "__main__" : 
   print("--- Jour 23 : Coprocessor Conflagration ---")
   with open("2015/jour23/input.txt") as f :
      data = f.readlines()
      data = [x.strip() for x in data]
      print(data)
      registre = calcule(data,{"a":0,"b":0})

   print("Part 1 : ",registre["b"])
   registre = calcule(data,{"a":1,"b":0})
   print("Part 2 : ",registre["b"])