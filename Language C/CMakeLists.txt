cmake_minimum_required(VERSION 3.20)
project(AdventureCode C)

# --- Configuration du compilateur ---
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

# Sources communes à tous les jours
set(COMMON_SOURCES
    utilities.c
)

# --- Macro pour ajouter facilement un jour ---
# Usage : add_day(2018 1)
macro(add_day year day)
    set(TARGET_NAME "solution_${year}_day${day}")
    set(DAY_DIR "${year}/day_${day}")
    set(SOURCE_FILE "${DAY_DIR}/solution.c")
    set(INPUT_FILE "${DAY_DIR}/input.txt")

    if(EXISTS "${CMAKE_SOURCE_DIR}/${SOURCE_FILE}")
        set(EXTRA_SOURCES "")

        # Day 16 utilise aussi registerOperation.c
        if(${year} EQUAL 2018 AND (${day} EQUAL 16 OR ${day} EQUAL 19))
            list(APPEND EXTRA_SOURCES 2018/enigmeUtilities/registerOperation.c)
        endif()

        add_executable(${TARGET_NAME}
            ${SOURCE_FILE}
            ${COMMON_SOURCES}
            ${EXTRA_SOURCES}
        )

        # Includes globaux utiles au projet
        target_include_directories(${TARGET_NAME} PRIVATE
            ${CMAKE_SOURCE_DIR}
            ${CMAKE_SOURCE_DIR}/2018/enigmeUtilities
        )

        message(STATUS "Ajout de l'exécutable : ${TARGET_NAME}")

        # Si un fichier input.txt existe, on le copie à côté de l'exécutable généré
        if(EXISTS "${CMAKE_SOURCE_DIR}/${INPUT_FILE}")
            add_custom_command(TARGET ${TARGET_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                "${CMAKE_SOURCE_DIR}/${INPUT_FILE}"
                "$<TARGET_FILE_DIR:${TARGET_NAME}>/input.txt"
            )
            message(STATUS "  -> Configuration de la copie automatique de input.txt")
        endif()
    else()
        message(WARNING "Fichier non trouvé : ${SOURCE_FILE}")
    endif()
endmacro()

# --- Liste des jours ---
add_day(2018 1)
add_day(2018 2)
add_day(2018 3)
add_day(2018 4)
add_day(2018 5)
add_day(2018 6)
add_day(2018 7)
add_day(2018 8)
add_day(2018 9)
add_day(2018 10)
add_day(2018 11)
add_day(2018 12)
add_day(2018 13)
add_day(2018 14)
add_day(2018 15)
add_day(2018 16)
add_day(2018 17)
add_day(2018 18)
add_day(2018 19)
add_day(2018 20)
add_day(2018 21)
add_day(2018 22)
add_day(2018 23)
add_day(2018 24)
add_day(2018 25)