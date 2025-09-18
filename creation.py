import os


def create_loop(x):
    for i in range(1,26):
        path = f".\\\{x}\\\jour{i}"
        os.mkdir(path)
        with open(path+"\\input.txt","w") as f :
            pass    
        with open(path+"\\sol.py","w") as f :
            f.write('# -*- coding: utf-8 -*- \n')
            f.write('if __name__ == "__main__" : \n')
            f.write(f'  print("--- Jour {i} : Solution ---") \n')
            f.write(f'  with open("{path+"\\\input.txt"}","r") as f : \n')
            f.write('       data = f.read().splitlines() \n')
        

if __name__ == "__main__":
    x=""
    while x is not int :
        try:
            x = int(input('What year will be created ? '))
            os.mkdir(str(x))
            create_loop(x)
            break
        except ValueError:
            print("it's not a year")
            
    
    