# python
import os
import time


def _safe_write(path, content="", mode="w", attempts=3, delay=0.1, encoding="utf-8"):
    """Ecrit dans `path` avec réessais en cas d'erreur IO."""
    for attempt in range(attempts):
        try:
            with open(path, mode, encoding=encoding) as f:
                if content:
                    f.write(content)
            return True
        except OSError:
            if attempt < attempts - 1:
                time.sleep(delay)
                delay *= 2
            else:
                raise
    return None


def create_loop(year):
    base = str(year)
    os.makedirs(base, exist_ok=True)
    for i in range(1, 26):
        day_dir = os.path.join(base, f"jour{i}")
        os.makedirs(day_dir, exist_ok=True)

        input_path = os.path.join(day_dir, "input.txt")
        sol_path = os.path.join(day_dir, "sol.py")

        # fichier input vide
        _safe_write(input_path, "")

        # contenu stable pour sol.py : lit input.txt relatif à son dossier
        sol_content = (
            "# -*- coding: utf-8 -*-\n"
            "import os\n\n"
            "if __name__ == '__main__':\n"
            f"    print('--- Jour {i} : Solution ---')\n"
            "    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')\n"
            "    with open(input_path, 'r', encoding='utf-8') as f:\n"
            "        data = f.read().splitlines()\n"
            "    # TODO: implémenter la solution\n"
        )
        _safe_write(sol_path, sol_content)
        
if __name__ == "__main__":
    while True:
        try:
            year = int(input("What year will be created ? "))
            create_loop(year)
            print(f"Création terminée pour l'année {year}")
            break
        except ValueError:
            print("Ce n'est pas une année valide, réessayer.")
        except OSError as e:
            print(f"Erreur lors de la création des fichiers : {e}")
            break