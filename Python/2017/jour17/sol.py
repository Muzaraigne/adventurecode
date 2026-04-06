# -*- coding: utf-8 -*-

def part1(step, objective):
  res = [0]
  pos = 0
  for i in range(1, objective + 1):
    pos = (pos + step) % len(res)
    res.insert(pos + 1, i)
    pos = pos + 1
  idx = res.index(objective)
  return res[(idx + 1) % len(res)]

def part2(step, objective):
  pos = 0
  size = 1
  value_after_zero = None
  for i in range(1, objective + 1):
    pos = (pos + step) % size
    if pos == 0:
      value_after_zero = i
    pos = pos + 1
    size += 1
  return value_after_zero

if __name__ == "__main__" : 
  print("--- Jour 17 : Solution ---") 
  data = 301
  print(f"Test (step=3, objective=9): {part1(3, 9)}")
  result1 = part1(data, 2017)
  print(f"Partie 1 (step={data}, after 2017): {result1}")
  result2 = part2(data, 50_000_000)
  print(f"Partie 2 (step={data}, value after 0): {result2}")