# -*- coding: utf-8 -*- 
import json


def add_json(data):
   if isinstance(data,str) or isinstance(data,bool):
      return 0 
   elif isinstance(data,int):
      return data
   else:
      if isinstance(data,list):
         res=0
         for i in data :
            res+=add_json(i)
         return res
      else:
         res=0
         if "red" in data or "red" in data.values():
            return 0
         for k,v in data.items():
            res += add_json(v)
         return res
      


if __name__ == "__main__" : 
   print("jour 12 d'advent of code 2015") 

   with open('2015/jour12/input.json','r') as f :
      data = json.load(f)
   res = add_json(data)

   print(f"la somme de tout les nombres dans le documents est {res}")


