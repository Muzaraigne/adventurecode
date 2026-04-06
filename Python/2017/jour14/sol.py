# -*- coding: utf-8 -*- 
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
from jour10.sol import hashage_dense as knot_hash

def convert(chaine):
   res =[]
   for c in chaine : 
        binary_4bit = bin(int(c, 16))[2:].zfill(4) 
        res += [int(i) for i in binary_4bit]
   return res

def count_lines(line):
  return sum(line)

def count_grid(grid):
   res =0 
   for i in range(0,128):
       res += count_lines(grid[i])
   return res

def grid(data) : 
   grid=[]
   for i in range(128):
      grid.append(convert(knot_hash(data+'-'+str(i))))
   return grid 

def flood_fill(grid,r,c):
   R =128
   C= 128

   if r<0 or r>=R or c<0 or c>=C or grid[r][c]==0:
      return
   
   grid[r][c] =0

   flood_fill(grid,r+1,c)
   flood_fill(grid,r-1,c)
   flood_fill(grid,r,c+1)
   flood_fill(grid,r,c-1)

def count_region(grid) : 
   g =grid.copy()
   res =0 
   for i in range(len(g)):
      for j in range(len(g[i])):
         if g[i][j] == 1 :
            res +=1 
            flood_fill(g,i,j)
   return res
if __name__ == "__main__" : 
  print("--- Jour 14 : Solution ---") 
  data  = grid('hfdlxzhv')
  dt = grid("flqrgnkx")

print('----Partie 1 ----')
print(f'Test: {count_grid(dt)}')
print(f'Il y a {count_grid(data)} carrés occupés')  

print('----Partie 2 ----')
print(f'Test: {count_region(dt)}')
print(f'Il y a {count_region(data)} carrés occupés')  