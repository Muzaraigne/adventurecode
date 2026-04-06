# -*- coding: utf-8 -*- 
def calculer_code(my_obj) : 
   row = my_obj["row"] 
   col = my_obj["col"] 
   n = row + col - 1 
   code = 20151125 
   for i in range(1, n * (n - 1) // 2 + col) : 
      code = (code * 252533) % 33554393 
   return code

if __name__ == "__main__" : 
   print("--- Jour 25 : Laissez le neiger (Solution) ---") 
   my_obj = {"row": 2981, "col": 3075}
   print("Le code est : ", calculer_code(my_obj))
