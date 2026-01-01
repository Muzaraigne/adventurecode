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
    if (ferror(file)) {
        fprintf(stderr, "Erreur de lecture du fichier %s.\n", filename);
        free(buffer);
        fclose(file);
        exit(EXIT_FAILURE);
    }
    buffer[read_length] = '\0';

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

// Modification : Retourne le tableau (char**) et remplit le compteur via un pointeur (int*)
char** extractLines(const char* filename, int* count) {
    char* full_content = read_file(filename);
    char* cursor = full_content;

    int local_count = 0;
    char** lines = NULL;

    while (1) {
        char* line = my_strsep(&cursor, "\n");
        if (line == NULL) break;

        // Réallocation du tableau de pointeurs
        char** tmp = realloc(lines, sizeof(char*) * (local_count + 2));
        if (tmp == NULL) {
            free(full_content);
            // En cas d'erreur, on pourrait free(lines) ici
            return NULL;
        }
        lines = tmp;

        lines[local_count] = strdup(line);
        local_count++;
        lines[local_count] = NULL; // Toujours terminer par NULL par sécurité
    }

    free(full_content);

    if (count != NULL) {
        *count = local_count;
    }

    return lines;
}

void free_lines(char** lines) {
    if (lines == NULL) return;

    for (int i = 0; lines[i] != NULL; i++) {
        free(lines[i]);
    }
    free(lines);
}