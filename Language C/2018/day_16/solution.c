#include <stdio.h>
#include <stdlib.h>
#include "../../utilities.h"

int main(void) {
	char** input = extractLines("input.txt");
	if (input == NULL) return EXIT_FAILURE;

	// Ton code ici

	free_lines(input);
	return 0;
}
