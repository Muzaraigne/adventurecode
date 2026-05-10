# Advent of Code Solver - Java

## Structure du Projet

```
src/main/java/org/example/
├── core/
│   ├── Day.java                 # Interface pour chaque solution
│   ├── AocClient.java          # Client HTTP pour récupérer les inputs
│   ├── InputStorage.java       # Gestion du cache des inputs
│   ├── SolutionRegistry.java   # Découverte auto des solutions par réflexion
│   ├── SolutionRunner.java     # Exécution des solutions
│   └── ConsoleMenu.java        # Menu de sélection de l'année
├── years/
│   └── y2023/
│       └── Day01.java          # Exemple de solution
└── Main.java                    # Point d'entrée

inputs/                          # Cache des inputs (créé automatiquement)
├── 2023/
│   ├── day01.txt
│   ├── day02.txt
│   └── ...
└── 2024/
    ├── day01.txt
    └── ...
```

## Configuration

### 1. Définir le cookie de session AoC

```bash
# Windows PowerShell
$env:AOC_SESSION="votre_cookie_ici"

# Windows CMD
set AOC_SESSION=votre_cookie_ici

# Linux/Mac
export AOC_SESSION="votre_cookie_ici"
```

Vous pouvez récupérer votre cookie de session en :
1. Allez sur https://adventofcode.com
2. Ouvrez les DevTools (F12)
3. Allez dans l'onglet "Storage" → "Cookies" → "adventofcode.com"
4. Copiez la valeur de `session`

### 2. Ajouter une nouvelle solution

Créez un fichier dans `src/main/java/org/example/years/y{ANNÉE}/Day{DD}.java` :

```java
package org.example.years.y2024;

import org.example.core.Day;

public class Day01 implements Day {
    @Override
    public String partOne(String input) {
        // Votre solution pour la partie 1
        return "résultat";
    }

    @Override
    public String partTwo(String input) {
        // Votre solution pour la partie 2
        return "résultat";
    }

    @Override
    public int getDay() {
        return 1;
    }

    @Override
    public int getYear() {
        return 2024;
    }
}
```

## Utilisation

### Compiler

```bash
mvn clean compile
```

### Exécuter le projet

```bash
mvn exec:java -Dexec.mainClass="org.example.Main"
```

Ou construire un JAR exécutable :

```bash
mvn clean package
java -jar target/aoc-solver.jar
```

## Fonctionnalités

- ✅ Découverte automatique des solutions via réflexion
- ✅ Récupération automatique des inputs depuis adventofcode.com
- ✅ Cache des inputs localement
- ✅ Menu interactif pour sélectionner l'année
- ✅ JAR exécutable auto-contenu
- ✅ Utilise Java 11+ (HttpClient intégré, pas de dépendance externe pour HTTP)

## Dépendances

- `org.reflections:reflections:0.10.2` - Découverte dynamique des classes
- Java 17+

## Notes

- Les inputs sont stockés dans `inputs/{year}/day{dd}.txt`
- Le cookie de session est requis pour récupérer les inputs depuis AoC
- Chaque solution est exécutée automatiquement et affichée dans la console

