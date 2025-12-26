// language: c
// Fichier: `creation.c`

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#ifdef _WIN32
  #include <direct.h>
  #define MKDIR(p) _mkdir(p)
  #define CHDIR(p) _chdir(p)
#else
  #include <sys/stat.h>
  #include <unistd.h>
  #define MKDIR(p) mkdir(p, 0755)
  #define CHDIR(p) chdir(p)
#endif

void create_folder(const char* path) {
    if (MKDIR(path) != 0) {
        if (errno != EEXIST) {
            fprintf(stderr, "Impossible de créer le dossier %s : %s\n", path, strerror(errno));
            exit(EXIT_FAILURE);
        } else {
            fprintf(stderr, "Le dossier %s existe déjà.\n", path);
        }
    }
}
void create_loop(int n) {
    char path[64];
    int needed = snprintf(path, sizeof(path), "day_%d", n);
    if (needed < 0 || (size_t)needed >= sizeof(path)) {
        fprintf(stderr, "Chemin trop long pour day_%d\n", n);
        exit(EXIT_FAILURE);
    }
    create_folder(path);
    if (CHDIR(path) != 0) {
        fprintf(stderr, "Impossible de se placer dans le dossier %s : %s\n", path, strerror(errno));
        exit(EXIT_FAILURE);
    }

    FILE* file = fopen("input.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Impossible d'ouvrir `input.txt` en écriture : %s\n", strerror(errno));
        exit(EXIT_FAILURE);
    }
    fclose(file);

    FILE* file2 = fopen("solution.c", "w");
    if (file2 == NULL) {
        fprintf(stderr, "Impossible d'ouvrir `solution.c` en écriture : %s\n", strerror(errno));
        exit(EXIT_FAILURE);
    }

    fprintf(file2,
        "#include <stdio.h>\n"
        "#include <stdlib.h>\n"
        "#include \"../../utilities.h\"\n"
        "\n"
        "int main(void) {\n"
        "\tchar** input = extractLines(\"input.txt\");\n"
        "\tif (input == NULL) return EXIT_FAILURE;\n"
        "\n"
        "\t// Ton code ici\n"
        "\n"
        "\tfree_lines(input);\n"
        "\treturn 0;\n"
        "}\n");
    fclose(file2);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        return EXIT_FAILURE;
    }
    int n = (int)strtol(argv[1], NULL, 10);

    char path[64];
    int needed = snprintf(path, sizeof(path), "%d", n);
    if (needed < 0 || (size_t)needed >= sizeof(path)) {
        fprintf(stderr, "Chemin trop long pour%d\n", n);
        exit(EXIT_FAILURE);
    }
    create_folder(path);
    if (CHDIR(path) != 0) {
        fprintf(stderr, "Erreur chdir vers %s : %s\n", path, strerror(errno));
        exit(EXIT_FAILURE);
    }
    for (int i = 1; i <= 25; i++) {
        create_loop(i);
        if (CHDIR("..") != 0) {
            fprintf(stderr, "Impossible de revenir au dossier parent : %s\n", strerror(errno));
            exit(EXIT_FAILURE);
        }
    }
    return 0;
}