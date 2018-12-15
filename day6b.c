#include <stdio.h>
#include <stdlib.h>

#define XMAX  512
#define YMAX  512

struct Point {
	int		x;
	int		y;
};

int distance_to_point(int x, int y, int pointx, int pointy) {
	return ((abs(pointx-x)+abs(pointy-y)));
}

int main(int argc, char **argv) {
	FILE 		*infile;
	FILE 		*outfile;
	struct Point	pointlist[50];	
	int 		grid[XMAX][YMAX]={0};
	int 		x, y, i;

	infile = fopen("day6.txt", "r");
	if (!infile) {
		printf ("Can't open file\n");
		return 1;
	}
	for (i=0; i<50; i++) 
		fscanf (infile, "%d, %d\n", &(pointlist[i]).x, &(pointlist[i]).y);
	fclose (infile);

	for (y=0; y<YMAX; y++)
		for (x=0; x<XMAX; x++) {
			int sumofdistances = 0;
			for (i=0; i<50; i++)
				sumofdistances += distance_to_point(x, y, pointlist[i].x, pointlist[i].y);
			if (sumofdistances < 10000)
				grid[x][y] = 20;	
		}

	// sweet!  now painstakingly find the area of the qualifying region
	int areasize = 0; 
	for (y=0; y<YMAX; y++)
		for (x=0; x<XMAX; x++)
			if (grid[x][y] != 0)
				areasize++;
	// report the size
	printf ("\nThe size of the area with the sum of distances to each target less than 10,000 at each point is %d\n", areasize);

	outfile = fopen("day6b.pbm", "w");
	fprintf (outfile, "P1\n%d\n%d\n", XMAX, YMAX);
		for (y=0; y<YMAX; y++) {
			for (x=0; x<XMAX; x++) {
			fprintf(outfile, "%d ", grid[x][y] ? 0 : 1);
		}
		fprintf(outfile, "\n");
	}
	fclose(outfile);
}
		
	
