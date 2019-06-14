#include <stdio.h>
#include <math.h>
#include <string.h>

#define PUZZLE_INPUT 36000000

void factors(unsigned long number, unsigned long * factorlist, int arraysize) {
	memset(factorlist, 0, sizeof(unsigned long) * arraysize);
	unsigned long i;
	unsigned long searchlen;
	unsigned long cofactor;
	searchlen = (int) sqrt(number);
	for (i=1; i <= searchlen; i++) {
		if ((number % i) == 0) {
			*factorlist++ = i;
			cofactor = number / i;
			if (cofactor != i)
				*factorlist++ = cofactor;
		}
	}
}

unsigned long howmanypresentsdoesthehouseget(unsigned long house) {
	unsigned long factorlist[256];
	unsigned long presents = 0;
	unsigned long *elf;
	// printf ("Factors for %lu:\n", house);
	factors(house, factorlist, 256);
	elf = factorlist;
	while (*elf) {
		// printf ("  %lu", *elf);
		if (house <= (*elf * 50))
			presents += (*elf++);
		else
			elf++;
	}
	// printf ("\n");
	return presents * 11;
}

int main(int argc, char **argv) {
	unsigned long house = 1;
	unsigned long numpresents = 0;

	while (numpresents <= PUZZLE_INPUT) {
		// printf ("%lu presents delivered to house %lu\n", numpresents, house);
		house++;
		numpresents = howmanypresentsdoesthehouseget(house);
	}
	printf ("%lu\n", house);
}
