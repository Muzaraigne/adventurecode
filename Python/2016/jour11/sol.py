from collections import deque
from itertools import combinations

def is_valid(floors):
    for floor in floors:
        gens = {item[0] for item in floor if item[1] == 'G'}
        chips = {item[0] for item in floor if item[1] == 'M'}
        if gens and any(chip not in gens for chip in chips):
            return False
    return True

def serialize_state(elevator, floors):
    elements = {}
    for i, floor in enumerate(floors):
        for item in floor:
            elements.setdefault(item[0], [None, None])
            elements[item[0]][0 if item[1] == 'G' else 1] = i
    elements_tuple = tuple(sorted((tuple(pos) for pos in elements.values())))
    return (elevator, elements_tuple)

def get_neighbors(elevator, floors):
    items = floors[elevator]
    for num_to_move in [1, 2]:
        for combo in combinations(items, num_to_move):
            for direction in [-1, 1]:
                new_floor = elevator + direction
                if 0 <= new_floor < 4:
                    new_floors = [set(floor) for floor in floors]
                    new_floors[elevator] = new_floors[elevator] - set(combo)
                    new_floors[new_floor] = new_floors[new_floor] | set(combo)
                    if is_valid(new_floors):
                        yield new_floor, new_floors

def solve(initial_floors):
    initial_elevator = 0
    seen = set()
    queue = deque()
    initial_state = serialize_state(initial_elevator, initial_floors)
    queue.append((initial_elevator, initial_floors, 0))
    seen.add(initial_state)
    target_floor = 3
    all_items = set()
    for floor in initial_floors:
        all_items |= floor

    while queue:
        elevator, floors, steps = queue.popleft()
        if all(item in floors[target_floor] for item in all_items):
            return steps
        for new_elevator, new_floors in get_neighbors(elevator, floors):
            new_state = serialize_state(new_elevator, new_floors)
            if new_state not in seen:
                seen.add(new_state)
                queue.append((new_elevator, new_floors, steps + 1))
    return -1

initial_floors = [
    {('T', 'G'), ('T', 'M'), ('P', 'G'), ('S', 'G')},
    {('P', 'M'), ('S', 'M')},
    {('Pr', 'G'), ('Pr', 'M'), ('Ru', 'G'), ('Ru', 'M')},
    set()
]
# ... (tout le code précédent inchangé)

initial_floors_part2 = [
    {('T', 'G'), ('T', 'M'), ('P', 'G'), ('S', 'G'), ('E', 'G'), ('E', 'M'), ('D', 'G'), ('D', 'M')},
    {('P', 'M'), ('S', 'M')},
    {('Pr', 'G'), ('Pr', 'M'), ('Ru', 'G'), ('Ru', 'M')},
    set()
]


if __name__ == "__main__":
    print("--- Jour 11 : Solution optimisée ---")
    print("Minimum steps:", solve(initial_floors))
    print("Minimum steps part 2:", solve(initial_floors_part2))

