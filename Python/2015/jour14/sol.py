# -*- coding: utf-8 -*- 
# Advent of Code 2015 - Day 14
# https://adventofcode.com/2015/day/14

def part1(data):
   max_dist = 0
   for name, (speed, time, rest, parc, cycle) in data.items():
      dist = parc * (2503 // cycle)
      if 2503 % cycle > time:
         dist += parc
      else:
         dist += speed * (2503 % cycle)
      return max(max_dist, dist)
  
  
def part2(data):
    scores = {name: 0 for name in data.keys()}
    distances = {name: 0 for name in data.keys()}
    duration = 2503

    for t in range(1, duration + 1):
        max_dist_at_t = 0

        # Calculate distance for each reindeer at time t
        for name, (speed, time, rest, parc, cycle) in data.items():
            # The current time within the cycle
            rem_in_cycle = t % cycle
            if rem_in_cycle == 0:
                rem_in_cycle = cycle
            if rem_in_cycle <= time:
                distances[name] += speed
        max_dist_at_t = max(distances.values())
        for name, dist in distances.items():
            if dist == max_dist_at_t:
                scores[name] += 1
                
    return max(scores.values())

if __name__ == "__main__" : 
   print(" --- jour 14 ---")

   with open('2015/jour14/input.txt', 'r') as f:
      input = f.read().splitlines()

   data = {}
   for line in input:
      parts = line.split(' ')
      name = parts[0]
      speed = int(parts[3])
      time = int(parts[6])
      rest = int(parts[13])
      parc =speed*time
      cycle = time + rest
      data[name] = (speed, time, rest, parc, cycle)

   
   print("Partie 1 :", part1(data)," km")
   print("Partie 2 :", part2(data)," points")
   print(" --- fin jour 14 ---")
