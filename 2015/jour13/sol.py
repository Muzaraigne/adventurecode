# -*- coding: utf-8 -*-
import itertools
def merge_happy(dict):
    res={}
    for k,v in dict.items() :
        n1,n2=k
        res[(n1,n2)]=v+dict[(n2,n1)]
    return res


if __name__ == "__main__":
   print("réponse jour 13")

   with open("2015/jour13/input.txt","r" ) as f:
        lines = f.readlines()

   happyness={}

   for line in lines : 
        parts = line.split()
        name1=parts[0]
        name2=parts[len(parts)-1].strip('.')
        if parts[2] == "lose":
            happy = -int(parts[3])
        else:
            happy = int(parts[3])
        happyness[(name1,name2)] = happy

   happyness = merge_happy(happyness)
   person = set(c for pair in happyness.keys() for c in pair)
   
   for p in person:
         happyness[(p,"me")] = 0
         happyness[("me",p)] = 0
   person.add("me")
   max_happyness = 0
   for perm in itertools.permutations(person):
        current_happyness=0
        for i in range(len(perm)):
            if i<len(perm)-1:
               current_happyness += happyness[perm[i],perm[i+1]]
            else:
                current_happyness += happyness[perm[i],perm[0]]
        if current_happyness >max_happyness:
            max_happyness = current_happyness
            long=perm

   print(f"le bonheur max est : {max_happyness}")
   print(f"Le chemin correspondant est : {' -> '.join(long)}")