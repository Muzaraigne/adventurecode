total_original_length = 0
total_memory_chars = 0
total_encoded_length = 0

with open("2015/jour8/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        total_original_length += len(line)
        decoded_string = eval(line)
        total_memory_chars += len(decoded_string)

        # Calcul de la nouvelle longueur encodée
        new_length = 2  # Pour les guillemets de début et de fin
        for char in line:
            if char == '"' or char == '\\':
                new_length += 2  # Échappement
            else:
                new_length += 1
        
        # Ajout au total des longueurs encodées
        total_encoded_length += new_length


print(f"Total des caractères de code : {total_original_length}")
print(f"Total des caractères en mémoire : {total_memory_chars}")
print(f"La différence est : {total_original_length - total_memory_chars}")

print(f"Total encoded length: {total_encoded_length}")
print(f"Difference: {total_encoded_length - total_original_length}")