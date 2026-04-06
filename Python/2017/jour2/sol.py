# -*- coding: utf-8 -*- 

def result(data):
  checksum = 0 
  for li in data : 
    checksum += max(li)-min(li)
  return checksum

def calcul(line):
    for i in range(len(line)):
        for j in range(len(line)):
            if i == j:
                continue
            num1 = line[i]
            num2 = line[j]
            if num1 % num2 == 0:
                return num1 // num2

    return 0
      
def result2(data):
  checksum =0 
  for li in data : 
    checksum += calcul(li)
  return checksum
def test():
  t = result(data_test)
  t2 = result2(data_test2)
  if(t != 18):
    print(f'error : got{t} expeted 18')
  if (t2 != 9):
     print(f'error : got{t2} expeted 9')

if __name__ == "__main__" : 
  print("--- Jour 2 : Solution ---") 
  with open(".\\2017\\jour2\\input.txt","r") as f : 
    data = [[int(n) for n in line.split('\t')] for line in f.read().splitlines()]
  with open(".\\2017\\jour2\\test.txt","r") as f : 
    data_test = [[int(n) for n in line.split(' ')] for line in f.read().splitlines()]
  with open(".\\2017\\jour2\\test2.txt","r") as f : 
    data_test2 = [[int(n) for n in line.split(' ')] for line in f.read().splitlines()]
  
  test()
  print(f'Partie 1 : La somme de validation de notre entrée vaut {result(data)}')
  print(f'Partie 2 : La somme de validation de notre entrée vaut {result2(data)}')