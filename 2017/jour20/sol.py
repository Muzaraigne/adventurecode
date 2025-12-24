# -*- coding: utf-8 -*-
import pathlib
import sys

class Particle:
    def __init__(self,number, position, speed, acceleration):
        self.number = number
        self.position = position
        self.speed = speed
        self.acceleration = acceleration

    def update(self):
        self.speed[0] += self.acceleration[0]
        self.speed[1] += self.acceleration[1]
        self.speed[2] += self.acceleration[2]
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        self.position[2] += self.speed[2]
        return self

    def distance(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])



def parse_input(input_data):
    particles = []
    for i, line in enumerate(input_data):
        parts = line.split(", ")
        p = list(map(int, parts[0][3:-1].split(",")))
        v = list(map(int, parts[1][3:-1].split(",")))
        a = list(map(int, parts[2][3:-1].split(",")))
        particles.append(Particle(i, p, v, a))
    return particles


def find_closest_particle(particles, steps=1000): # Simulate for a number of steps
    for _ in range(steps):
        for particle in particles:
            particle.update()
    closest_particle = min(particles, key=lambda p: p.distance())
    return closest_particle.number

def update_collisions(particles):
    positions = {}
    for particle in particles:
        pos_tuple = tuple(particle.position)
        if pos_tuple not in positions:
            positions[pos_tuple] = []
        positions[pos_tuple].append(particle)

    # Remove particles that have collided
    remaining_particles = []
    for same_pos_particles in positions.values():
        if len(same_pos_particles) == 1:
            remaining_particles.append(same_pos_particles[0])

    return remaining_particles

def solve(input_data):
    particles = parse_input(input_data)
    closest_particle_number = find_closest_particle(particles)
    return closest_particle_number

# python
def solve2(input_data, max_steps=1000, stable_steps=40):
    particles = parse_input(input_data)
    prev_count = len(particles)
    stable = 0
    step = 0
    while step < max_steps and stable < stable_steps and len(particles) > 1:
        # mise à jour des positions
        updated = [p.update() for p in particles]
        # suppression des collisions
        particles = update_collisions(updated)
        # détection de stabilité du nombre de particules
        if len(particles) == prev_count:
            stable += 1
        else:
            stable = 0
            prev_count = len(particles)
        step += 1
    return len(particles) if particles else None


def test():
    test_data = [
        "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>",
        "p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"
    ]
    assert solve(test_data) == 0
    print("All tests passed.")
def test2():
    test_data = [
        "p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>",
        "p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>",
        "p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>",
        "p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"
    ]
    remaining_particle = solve2(test_data)
    assert remaining_particle == 1
    print("All tests for part 2 passed.")

if __name__ == "__main__":
    print("--- Jour 20 : Solution ---")
    base = pathlib.Path(__file__).resolve().parent
    input_path = base / "input.txt"  # fichier dans le même dossier que `sol.py`
    try:
        with input_path.open("r", encoding="utf-8") as f:
            data = f.read().splitlines()
    except FileNotFoundError:
        print(f"Fichier introuvable: {input_path}")
        sys.exit(1)
    test()
    test2()
    result_part1 = solve(data) # use a default of 1000 steps
    result_part2 = solve2(data)
    print(f"Result Part 1 : {result_part1}")
    print(f"Result Part 2 : {result_part2}")