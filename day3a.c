#include <stdio.h>

int main (int argc, char **argv) {
	FILE * infile, * outfile;
	char cloth[1000][1000] = {0};
	int num, x, y, startx, starty, width, height; 
	int collisioninches=0;
	int mostoverlap=0;
	infile = fopen("day3.txt", "r");
	while (fscanf(infile, "#%d @ %d,%d: %dx%d\n", &num, &startx, &starty, &width, &height) != EOF) {
		// printf("Number %d, starting at %d, %d, %dx%d\n", num, startx, starty, width, height);
		for (y=starty; y<starty+height; y++)
			for (x=startx; x<startx+width; x++) {
				cloth[x][y]++;
				if (cloth[x][y] > mostoverlap)
					mostoverlap = cloth[x][y];
			}	
	}
	fclose(infile);
	outfile = fopen("day3a.pgm", "w");
	fprintf (outfile, "P2\n1000\n1000\n%d\n", mostoverlap);
	for (y=0; y<1000; y++) {
		for (x=0; x<1000; x++) {
			if (cloth[x][y]>1)
				collisioninches++;
			fprintf(outfile, "%d ", cloth[x][y]);
		}
		fprintf(outfile, "\n");
	}
	fclose(outfile);
	printf ("%d inches of cloth are in contention\n", collisioninches);
}
