# -*- coding: utf-8 -*- 
from collections import defaultdict, deque

def get_value(registers, x):
    try:
        return int(x)
    except ValueError:
        return registers[x]

def part1(instructions):
    registers = defaultdict(int)
    pc = 0  
    last_sound = None
    
    while 0 <= pc < len(instructions):
        parts = instructions[pc].split()
        op = parts[0]
        
        if op == "snd":
            last_sound = get_value(registers, parts[1])
        elif op == "set":
            registers[parts[1]] = get_value(registers, parts[2])
        elif op == "add":
            registers[parts[1]] += get_value(registers, parts[2])
        elif op == "mul":
            registers[parts[1]] *= get_value(registers, parts[2])
        elif op == "mod":
            registers[parts[1]] %= get_value(registers, parts[2])
        elif op == "rcv":
            if get_value(registers, parts[1]) != 0:
                return last_sound
        elif op == "jgz":
            if get_value(registers, parts[1]) > 0:
                pc += get_value(registers, parts[2])
                continue
        
        pc += 1
    
    return last_sound

def part2(instructions):
    programs = [
        {"id": 0, "registers": defaultdict(int), "queue": deque(), "pc": 0, "sent": 0},
        {"id": 1, "registers": defaultdict(int), "queue": deque(), "pc": 0, "sent": 0}
    ]
    programs[0]["registers"]["p"] = 0
    programs[1]["registers"]["p"] = 1
    
    waiting = [False, False]
    
    while True:
        deadlock = True
        
        for pid in [0, 1]:
            prog = programs[pid]
            other = programs[1 - pid]
            
            if waiting[pid]:
                if prog["queue"]:
                    waiting[pid] = False
                else:
                    continue
            while 0 <= prog["pc"] < len(instructions):
                parts = instructions[prog["pc"]].split()
                op = parts[0]
                
                if op == "snd":
                    val = get_value(prog["registers"], parts[1])
                    other["queue"].append(val)
                    prog["sent"] += 1
                elif op == "set":
                    prog["registers"][parts[1]] = get_value(prog["registers"], parts[2])
                elif op == "add":
                    prog["registers"][parts[1]] += get_value(prog["registers"], parts[2])
                elif op == "mul":
                    prog["registers"][parts[1]] *= get_value(prog["registers"], parts[2])
                elif op == "mod":
                    prog["registers"][parts[1]] %= get_value(prog["registers"], parts[2])
                elif op == "rcv":
                    if prog["queue"]:
                        prog["registers"][parts[1]] = prog["queue"].popleft()
                    else:
                        waiting[pid] = True
                        break
                elif op == "jgz":
                    if get_value(prog["registers"], parts[1]) > 0:
                        prog["pc"] += get_value(prog["registers"], parts[2])
                        continue
                
                prog["pc"] += 1
            
            if not waiting[pid] or prog["queue"]:
                deadlock = False
        
        if (waiting[0] and not programs[0]["queue"] and 
            waiting[1] and not programs[1]["queue"]):
            break
        if (programs[0]["pc"] < 0 or programs[0]["pc"] >= len(instructions)) and \
           (programs[1]["pc"] < 0 or programs[1]["pc"] >= len(instructions)):
            break
    
    return programs[1]["sent"]

if __name__ == "__main__" : 
    print("--- Jour 18 : Solution ---") 
    with open(".\\2017\\jour18\\input.txt","r") as f : 
        data = f.read().splitlines()
    
    result1 = part1(data)
    print(f"Partie 1 (première fréquence récupérée): {result1}")
    
    result2 = part2(data)
    print(f"Partie 2 (nombre d'envois du programme 1): {result2}") 
