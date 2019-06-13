#include <stdio.h>

#define PUZZLE_INPUT 36000000

unsigned long howmanypresentsdoesthehouseget(unsigned long house) {
	unsigned long presents = 0;
	unsigned long elf;
	for (elf=house; elf>0; elf--) {
		if (((house % elf) == 0) && ((elf * 50) <= house)) {
			presents += (elf*11);
		}
	}
	return presents;
}

int main(int argc, char **argv) {
	unsigned long house = 2035958;
	unsigned long numpresents = 0;
	while (numpresents <= PUZZLE_INPUT) {
		// printf ("%lu presents delivered to house %lu\n", numpresents, house);
		house++;
		numpresents = howmanypresentsdoesthehouseget(house);
	}
	printf ("%lu\n", house);
}
