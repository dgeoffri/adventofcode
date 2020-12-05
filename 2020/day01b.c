#include <stdio.h>

int readfile(FILE *inf, int *values, int num) {
	int reccount = 0;
	while ((fscanf(inf, "%d\n", &values[reccount]) != EOF) && reccount <= num) {
		reccount++;
	}
	reccount--;
	return reccount;
}

void findcombo(int *values, int num) {
	int i, j, k;
	for (i = 0; i <= num; i++) {
		for (j = i + 1; j <= num; j++) {
			for (k = j + 1; k <= num; k++) {
				int x, y, z;
				x = values[i];
				y = values[j];
				z = values[k];
				if (x + y + z == 2020) {
					printf ("%d, %d, and %d sum to 2020:  their product is %d\n", x, y, z, x * y * z);
					return;
				}
			}
		}
	}
}

int main(int argc, char **argv) {
	FILE *inputfile;
	int vals[256];
	int i = 0;
	int count = 0;

	inputfile = fopen("day01.txt", "r");
	count = readfile(inputfile, vals, sizeof(vals) / sizeof(vals[0]));
	fclose(inputfile);

	// printvals(vals, count);
	
	findcombo(vals, count);
}


