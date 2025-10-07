# -*- coding: utf-8 -*- 
# -*- coding: utf-8 -*- 

from logging import root


def transmute(data):
    """
    Analyse les données brutes en un dictionnaire de nœuds, 
    en définissant les attributs 'name', 'weight', 'children', et 'parent'.
    """
    nodes = dict()
    
    
    for d in data:
        parts = d.split(' ')
        name = parts[0]
        weight = int(parts[1].strip('()'))
        
        node_info = {
            'name': name,
            'weight': weight, 
            'children': [],   
            'parent': None    
        }
        
        if len(parts) > 2 and parts[2] == '->':
            node_info['children'] = [l.strip(',') for l in parts[3:]]
        
        nodes[name] = node_info
        
    
    for name, info in nodes.items():
        for child_name in info['children']:
            if child_name in nodes:
                nodes[child_name]['parent'] = name
            
    return nodes

def find_root(nodes):
    """Trouve le nom du programme qui est la racine de l'arbre."""
    for name, info in nodes.items():
        if info['parent'] is None:
            return name
    return None

def calculate_total_weight(node_name, nodes):
    """
    Calcule le poids total (poids propre + poids des sous-arbres) pour un nœud donné
    et le stocke dans 'total_weight'.
    """
    node = nodes[node_name]
    
    if 'total_weight' in node:
        return node['total_weight']
    
    total = node['weight']
    
    for child_name in node['children']:
        total += calculate_total_weight(child_name, nodes)
        
    node['total_weight'] = total
    return total

def find_unbalanced_and_fix(root_name, nodes):
    """
    Parcourt l'arbre pour trouver le nœud déséquilibré et calcule son poids corrigé.
    """
    current_name = root_name
    
    while True:
        current_node = nodes[current_name]
        
        if not current_node['children']:
            break
            
        weights_map = {} 
        for child_name in current_node['children']:
            weight = nodes[child_name]['total_weight']
            weights_map.setdefault(weight, []).append(child_name)
        if len(weights_map) == 1:
            break
        correct_weight = 0
        intruder_weight = 0
        intruder_name = None
        
        for weight, children_list in weights_map.items():
            if len(children_list) == 1:
                intruder_name = children_list[0]
                intruder_weight = weight
            else:
                correct_weight = weight
        current_name = intruder_name
    
    difference = intruder_weight - correct_weight
    unbalanced_node_weight = nodes[intruder_name]['weight']
    new_weight = unbalanced_node_weight - difference
    
    return new_weight



if __name__ == "__main__" : 
  print("--- Jour 7 : Solution ---") 
  with open(".\\2017\\jour7\\input.txt","r") as f : 
    data = f.read().splitlines() 

  with open(".\\2017\\jour7\\test.txt","r") as f : 
    d_test = f.read().splitlines()
  nodes = transmute(data)
  root_name = find_root(nodes)
  print(f'Sur l \'exemple on a : {find_root(transmute(d_test))}')
  print(f"\nPartie 1: Le programme racine est : { root_name}")

  calculate_total_weight(root_name, nodes)
        
        
  corrected_weight = find_unbalanced_and_fix(root_name, nodes)

  print(f"Partie 2: Le poids correct du programme déséquilibré doit être : {corrected_weight}")
