# -*- coding: utf-8 -*- 
def is_anagram(s1,s2):
  return "".join(sorted(s1)) == "".join(sorted(s2))

def have_anagram(line):
  line = line.split(' ')
  for i in range(0,len(line)-1) : 
    for j in range (i+1,len(line)):
      if is_anagram(line[i],line[j]):
        return False
  return True


def is_valid_password (line) : 
  line = line.split(' ')
  res= dict()
  for li in line : 
    if res.get(li,0)==0 :
      res[li]=1
    else : 
      return False
  return True

def resolve_part_1(data):
  acc = 0 
  for d in data : 
    if is_valid_password(d):
      acc +=1
  return acc

def resolve_part_2(data):
  acc =0
  for d in data :
    if is_valid_password(d) and have_anagram(d):
      acc +=1
  return acc


def test():
  for i in ["aa bb cc dd ee ","aa bb cc dd aa ","aa bb cc dd aaa "]:
    print(f'{i} est valide : {is_valid_password(i)}')

  for i in ["abcde fghij","abcde xyz ecdab","a ab abc abd abf abj","iiii oiii ooii oooi oooo","oiii ioii iioi iiio"]:
    print(f'{i} est valide : {is_valid_password(i) and have_anagram(i)}')


if __name__ == "__main__" : 
  print("--- Jour 4 : Solution ---") 
  with open(".\\2017\\jour4\\input.txt","r") as f : 
    data = f.read().splitlines() 
  test()

  print(f"Partie 1 : Il y a {resolve_part_1(data)} mot de passe valide")
  print(f'Partie 2 : Il y a {resolve_part_2(data)} mot de passe valide')