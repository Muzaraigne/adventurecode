# --- Configuration par défaut ---
CC = gcc
CFLAGS = -Wall -Wextra -std=gnu11 -I.

# Tu peux changer ces valeurs ici ou les passer en ligne de commande
YEAR ?= 2018
DAY ?= 1

# Fichiers
UTILS_SRC = utilities.c
UTILS_OBJ = $(UTILS_SRC:.c=.o)

# Chemin vers la solution cible
TARGET_DIR = $(YEAR)/day_$(DAY)
TARGET_EXE = $(TARGET_DIR)/solution.exe
TARGET_SRC = $(TARGET_DIR)/solution.c

# --- Règles ---

# Par défaut, on affiche l'aide
help:
	@echo "Usage:"
	@echo "  mingw32-make            : Compile la solution du jour $(DAY) de l'annee $(YEAR)"
	@echo "  mingw32-make run        : Compile et execute le jour $(DAY)"
	@echo "  mingw32-make all_year   : Compile tous les jours de l'annee $(YEAR)"
	@echo "  Options : YEAR=2018 DAY=5"

# Règle pour compiler la solution spécifique (YEAR/DAY)
$(TARGET_EXE): $(TARGET_SRC) $(UTILS_OBJ)
	@echo "--- Compilation de $(TARGET_EXE) ---"
	$(CC) $(CFLAGS) $^ -o $@

# Compiler les utilitaires
$(UTILS_OBJ): $(UTILS_SRC)
	$(CC) $(CFLAGS) -c $< -o $@

# EXECUTER : Compile si besoin, puis lance
run: $(TARGET_EXE)
	@echo "--- Execution du Jour $(DAY) ($(YEAR)) ---"
	@cd $(TARGET_DIR) && .\solution.exe

# TOUT COMPILER pour une année donnée
all_year: $(UTILS_OBJ)
	@echo "--- Compilation de tous les jours de $(YEAR) ---"
	@for /L %%i in (1,1,25) do @( \
		if exist $(YEAR)\day_%%i\solution.c ( \
			gcc $(CFLAGS) $(YEAR)\day_%%i\solution.c $(UTILS_OBJ) -o $(YEAR)\day_%%i\solution.exe \
		) \
	)

clean:
	del /S /Q *.o *.exe

.PHONY: help run all_year clean