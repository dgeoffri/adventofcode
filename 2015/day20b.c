#include <stdio.h>
#include <math.h>
#include <string.h>

#define PUZZLE_INPUT 36000000

void factors(unsigned long number, unsigned long * factorlist, int arraysize) {
    memset(factors, 0, sizeof(unsigned long) * arraysize);
    int i;
    int searchlen;
    unsigned long cofactor;
    searchlen = (int) sqrt(number);
    for (i=0; i <= searchlen; i++) {
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
    unsigned long *elf = factorlist;
    factors(house, factorlist, 256);
    while (*elf)
        presents += *elf++;
	return presents;
}

int main(int argc, char **argv) {
	unsigned long house = 1;
	unsigned long numpresents = 0;
    
    while (numpresents <= PUZZLE_INPUT) {
		printf ("%lu presents delivered to house %lu\n", numpresents, house);
		house++;
		numpresents = howmanypresentsdoesthehouseget(house);
	}
	printf ("%lu\n", house);
}
