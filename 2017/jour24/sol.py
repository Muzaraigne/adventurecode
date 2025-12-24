# -*- coding: utf-8 -*-
import os

if __name__ == "__main__" :
  print("--- Jour 24 : Solution ---") 
  input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
  with open(input_path, 'r', encoding='utf-8') as f:
       data = f.read().splitlines() 
