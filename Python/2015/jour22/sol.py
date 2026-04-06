from collections import deque
import copy

# Statistiques du jeu
player = {"hp": 50, "mana": 500}
boss = {"hp": 55, "dmg": 8}
spell = {
    "missile": {"cost": 53, "dmg": 4, "heal": 0, "turn": 1},
    "soin": {"cost": 73, "dmg": 2, "heal": 2, "turn": 1},
    "bouclier": {"cost": 113, "dmg": 0, "heal": 0, "armor": 7, "turn": 6},
    "poison": {"cost": 173, "dmg": 3, "heal": 0, "turn": 6},
    "recharge": {"cost": 229, "dmg": 0, "heal": 0, "mana": 101, "turn": 5}
}

# Fonction pour appliquer les effets persistants
def apply_effects(state):
    """
    Applique les effets persistants (poison, bouclier, recharge) sur l'état du jeu.
    Retourne la valeur d'armure pour le tour en cours.
    """
    armor = 0
    
    # Effet poison
    if state["effects"]["poison"] > 0:
        state["boss_hp"] -= spell["poison"]["dmg"]
        state["effects"]["poison"] -= 1
    
    # Effet bouclier
    if state["effects"]["bouclier"] > 0:
        armor = spell["bouclier"]["armor"]
        state["effects"]["bouclier"] -= 1
    
    # Effet recharge
    if state["effects"]["recharge"] > 0:
        state["player_mana"] += spell["recharge"]["mana"]
        state["effects"]["recharge"] -= 1
        
    return armor



def find_min_cost(player_stats, boss_stats, hard_mode=False):
    queue = deque()
    
    initial_state = {
        "player_hp": player_stats["hp"],
        "player_mana": player_stats["mana"],
        "boss_hp": boss_stats["hp"],
        "mana_spent": 0,
        "effects": {"poison": 0, "bouclier": 0, "recharge": 0},
    }
    
    queue.append(initial_state)
    
    min_mana_found = float('inf')

    while queue:
        current_state = queue.popleft()
        
        # 1. Tour du joueur
        
        # Mode difficile
        if hard_mode:
            current_state["player_hp"] -= 1
            if current_state["player_hp"] <= 0:
                continue

        # Application des effets
        apply_effects(current_state)

        # Vérification si le boss est déjà vaincu par les effets
        if current_state["boss_hp"] <= 0:
            min_mana_found = min(min_mana_found, current_state["mana_spent"])
            continue

        # 2. Simulation du choix de sort pour le joueur
        for s_name, s_data in spell.items():
            if current_state["player_mana"] < s_data["cost"] or \
               (s_name in current_state["effects"] and current_state["effects"][s_name] > 0):
                continue

            new_state = copy.deepcopy(current_state)
            new_state["player_mana"] -= s_data["cost"]
            new_state["mana_spent"] += s_data["cost"]
            
            if s_name == "missile":
                new_state["boss_hp"] -= s_data["dmg"]
            elif s_name == "soin":
                new_state["boss_hp"] -= s_data["dmg"]
                new_state["player_hp"] += s_data["heal"]
            else:
                new_state["effects"][s_name] = s_data["turn"]
            
            if new_state["boss_hp"] <= 0:
                min_mana_found = min(min_mana_found, new_state["mana_spent"])
                continue

            # 3. Tour du boss
            
            # Application des effets de fin de tour
            armor_boss_turn = apply_effects(new_state)
            
            if new_state["boss_hp"] <= 0:
                min_mana_found = min(min_mana_found, new_state["mana_spent"])
                continue
            
            # Attaque du boss
            damage = max(1, boss_stats["dmg"] - armor_boss_turn)
            new_state["player_hp"] -= damage
            
            # Vérification si le joueur survit
            if new_state["player_hp"] > 0:
                if new_state["mana_spent"] < min_mana_found:
                    queue.append(new_state)

    return min_mana_found

# ---

if __name__ == "__main__":
    min_mana_part1 = find_min_cost(player, boss, hard_mode=False)
    print("Part 1: Le nombre de mana minimum pour gagner est", min_mana_part1)

    min_mana_part2 = find_min_cost(player, boss, hard_mode=True)
    print("Part 2: Le nombre de mana minimum pour gagner est", min_mana_part2)