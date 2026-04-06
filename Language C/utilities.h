//
// Created by Louis on 26/12/2025.
//

#ifndef ADVENTURECODE_UTILITIES_H
#define ADVENTURECODE_UTILITIES_H
char* read_file(const char* filename);
char** extractLines(const char* filename, int* count);
void free_lines(char** lines);
#endif //ADVENTURECODE_UTILITIES_H