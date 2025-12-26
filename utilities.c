//
// Created by Louis on 26/12/2025.
//
#include "utilities.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* read_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Impossible d'ouvrir le fichier %s en lecture.\n", filename);
        exit(EXIT_FAILURE);
    }

    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* buffer = (char*)malloc(length + 1);
    if (buffer == NULL) {
        fprintf(stderr, "Erreur d'allocation mémoire.\n");
        fclose(file);
        exit(EXIT_FAILURE);
    }

    size_t read_length = fread(buffer, 1, length, file);
    if (read_length != length) {
        fprintf(stderr, "Erreur de lecture du fichier %s.\n", filename);
        free(buffer);
        fclose(file);
        exit(EXIT_FAILURE);
    }
    buffer[length] = '\0';

    fclose(file);
    return buffer;
}

char* my_strsep(char** stringp, const char* delim) {
    char* start = *stringp;
    char* p;

    if (start == NULL) return NULL;

    p = strpbrk(start, delim);
    if (p) {
        *p = '\0';
        *stringp = p + 1;
    } else {
        *stringp = NULL;
    }

    return start;
}
char** extractLines(const char* filename) {
    char* full_content = read_file(filename);
    char* cursor = full_content;
    char** lines = NULL;
    size_t count = 0;

    while (1) {
        char* line = my_strsep(&cursor, "\n");
        if (line == NULL) break;


        char** tmp = realloc(lines, sizeof(char*) * (count + 2));
        if (tmp == NULL) {
            free(full_content);
            return lines;
        }
        lines = tmp;

        lines[count] = strdup(line);
        count++;
        lines[count] = NULL;
    }

    free(full_content); // On peut maintenant libérer le buffer global
    return lines;
}

void free_lines(char** lines) {
    if (lines == NULL) return;

    for (int i = 0; lines[i] != NULL; i++) {
        free(lines[i]); // Libère chaque chaîne de caractères (allouée par strdup)
    }
    free(lines); // Libère le tableau de pointeurs lui-même (alloué par realloc)
}