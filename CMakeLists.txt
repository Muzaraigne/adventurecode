cmake_minimum_required(VERSION 3.20)
project(AdventureCode C)

# --- Configuration du compilateur ---
# Utilisation de C11 avec extensions (équivalent à -std=gnu11)
# Cela corrige les warnings/erreurs sur strdup
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

# Inclure le dossier racine pour que les #include "utilities.h" fonctionnent
include_directories(${CMAKE_SOURCE_DIR})

# Fichiers sources communs à tous les jours
set(COMMON_SOURCES utilities.c)

# --- Macro pour ajouter facilement un jour ---
# Usage : add_day(2018 1)
macro(add_day year day)
    set(TARGET_NAME "solution_${year}_day${day}")
    set(SOURCE_FILE "${year}/day_${day}/solution.c")

    if(EXISTS "${CMAKE_SOURCE_DIR}/${SOURCE_FILE}")
        add_executable(${TARGET_NAME} ${SOURCE_FILE} ${COMMON_SOURCES})
        message(STATUS "Ajout de l'exécutable : ${TARGET_NAME}")
    else()
        message(WARNING "Fichier non trouvé : ${SOURCE_FILE}")
    endif()
endmacro()

# --- Liste des jours ---
# Ajoutez une ligne ici pour chaque nouveau jour que vous résolvez
add_day(2018 1)