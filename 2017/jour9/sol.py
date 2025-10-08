# -*- coding: utf-8 -*- 

def compute (data):
  total = 0 
  acc = 0 
  i =0
  while i < (len(data)) : 
    c = data[i]
    if c == '{' : 
      acc += 1
    if c == '}' :
      total += acc
      acc -= 1
    if c == '<' : 
      while data[i] != ">" and i < len(data):
        if data[i] == "!":
          i +=1
        i +=1
    if c == '!':
      i +=1
    i +=1
  if acc !=0 :
    return total +acc
  return total

def deleted(data):
  total = 0 
  i =0
  while i < (len(data)) : 
    c = data[i]
    if c == '<' : 
      i+=1
      while data[i] != ">" and i < len(data):
        if data[i] == "!":
          i+=1
        else : 
          total +=1
        i+=1
    i +=1
  return total

def test() : 
  data = [
    '{}',
    '{{{}}}',
    "{{},{}}",
    "{{{},{},{{}}}}",
    "{<a>,<a>,<a>,<a>}",
    "{{<ab>},{<ab>},{<ab>},{<ab>}}",
    "{{<!!>},{<!!>},{<!!>},{<!!>}}",
    "{{<a!>},{<a!>},{<a!>},{<ab>}}"
  ]
  responde =[1,6,5,16,1,9,9,3]
  for i in range(len(data)):
    res = compute(data[i])
    if res != responde[i] :
      print(f'error, we espected {responde[i]}, we got {res}')

  data2 =[
    
    "<>", 
    "<random characters>", 
    "<<<<>", 
    "<{!>}>",
    "<!!>",
    "<!!!>>", 
    "<{o\"i!a,<{i<a>"

  ]
  rep2 =[0,17,3,2,0,0,10]
  for i in range(len(data2)):
    res = deleted(data2[i])
    if res != rep2[i] :
      print(f'error, we espected {rep2[i]}, we got {res}')


if __name__ == "__main__" : 
  print("--- iour 9 : Solution ---") 
  with open(".\\2017\\jour9\\input.txt","r") as f : 
    data = f.read()
  test()
  print(f'Partie 1 : The total of score of my stream is {compute(data)}')
  print(f'Partie 2 : The total non-canceled characters are within the garbage is {deleted(data)}')
