# -*- coding: utf-8 -*-

def parse_line(line):
    parts = line.split()
    name = parts[0]  
    size = int(parts[1][:-1])
    used = int(parts[2][:-1])
    avail = int(parts[3][:-1])
    _, x_str, y_str = name.split('-')
    x = int(x_str[1:])
    y = int(y_str[1:])
    return {
        "x": x,
        "y": y,
        "size": size,
        "used": used,
        "avail": avail,
    }

def count_viable_pairs(nodes):
    count = 0
    for a in nodes:
        for b in nodes:
            if a == b:
                continue
            if a["used"] > 0 and a["used"] <= b["avail"]:
                count += 1
    return count

if __name__ == "__main__":
    print("--- Jour 22 : Solution ---")

    # --- Test mini dataset ---
    test_nodes = [
        {"x": 0, "y": 0, "size": 10, "used": 8, "avail": 2},
        {"x": 0, "y": 1, "size": 11, "used": 0, "avail": 11},
        {"x": 1, "y": 0, "size": 9,  "used": 6, "avail": 3},
        {"x": 1, "y": 1, "size": 12, "used": 7, "avail": 5},
    ]

    print("Test count_viable_pairs (doit afficher 3):", count_viable_pairs(test_nodes))

    # --- Lecture du vrai input ---
    with open(".\\2016\\jour22\\input.txt", "r") as f:
        data = f.read().splitlines()

    nodes = [parse_line(line) for line in data[2:]]

    # --- Partie 1 ---
    viable_pairs = count_viable_pairs(nodes)
    print("Partie 1 :", viable_pairs)

    # --- Partie 2 ---
    max_x = max(node["x"] for node in nodes)
    max_y = max(node["y"] for node in nodes)
    empty_node = next(node for node in nodes if node["used"] == 0)
    goal_node = next(node for node in nodes if node["x"] == max_x and node["y"] == 0)
    wall_threshold = empty_node["size"]
    walls = set((node["x"], node["y"]) for node in nodes if node["used"] > wall_threshold)
    vx, vy = empty_node["x"], empty_node["y"]
    gx, gy = goal_node["x"], goal_node["y"]
    steps_to_goal_left = abs(vx - (gx-1)) + abs(vy - gy)
    total_steps = steps_to_goal_left + 5 * gx

    print("Partie 2 (nombre de mouvements minimum approximatif) :", total_steps)
