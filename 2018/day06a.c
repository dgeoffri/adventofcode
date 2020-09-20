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

	infile = fopen("day06.txt", "r");
	if (!infile) {
		printf ("Can't open file\n");
		return 1;
	}
	for (i=0; i<50; i++) 
		fscanf (infile, "%d, %d\n", &(pointlist[i]).x, &(pointlist[i]).y);
	fclose (infile);

	for (y=0; y<YMAX; y++)
		for (x=0; x<XMAX; x++) {
			int closestpoint = 1;
			int closestdistance = distance_to_point(x, y, pointlist[0].x, pointlist[0].y);
			for (i=1; i<50; i++)
				if (distance_to_point(x, y, pointlist[i].x, pointlist[i].y) < closestdistance) {
					closestpoint = i+1;
					closestdistance = distance_to_point(x, y, pointlist[i].x, pointlist[i].y);
				} else if (distance_to_point(x, y, pointlist[i].x, pointlist[i].y) == closestdistance)
					closestpoint = 0;
			grid[x][y] = closestpoint;
		}

	// Disqualify any region that touches an edge
	// -- top edge
	for (x=0; x<XMAX; x++)
		if (grid[x][0] != 0) {
			// Sweep the field of this region
			int region = grid[x][0];
			int x1, y1;
			for (y1=0; y1<YMAX; y1++)
				for (x1=0; x1<XMAX; x1++)
					if (grid[x1][y1] == region)
						grid[x1][y1] = 0;
		}

	// -- left edge
	for (y=0; y<YMAX; y++)
		if (grid[0][y] != 0) {
			// Sweep the field of this region
			int region = grid[0][y];
			int x1, y1;
			for (y1=0; y1<XMAX; y1++)
				for (x1=0; x1<YMAX; x1++)
					if (grid[x1][y1] == region)
						grid[x1][y1] = 0;
		}

	// -- right edge
	for (y=0; y<YMAX; y++)
		if (grid[XMAX-1][y] != 0) {
			// Sweep the field of this region
			int region = grid[XMAX-1][y];
			int x1, y1;
			for (y1=0; y1<XMAX; y1++)
				for (x1=0; x1<YMAX; x1++)
					if (grid[x1][y1] == region)
						grid[x1][y1] = 0;
		}

	// -- bottom edge
	for (x=0; x<XMAX; x++)
		if (grid[x][YMAX-1] != 0) {
			// Sweep the field of this region
			int region = grid[x][YMAX-1];
			int x1, y1;
			for (y1=0; y1<XMAX; y1++)
				for (x1=0; x1<YMAX; x1++)
					if (grid[x1][y1] == region)
						grid[x1][y1] = 0;
		}

	// sweet!  now painstakingly find the areas for each remaining region
	int areasizes[50] = {0};
	for (y=0; y<YMAX; y++)
		for (x=0; x<XMAX; x++)
			if (grid[x][y] != 0)
				areasizes[(grid[x][y])-1]++;
	// show them all
	int largestarea = 0;
	int largestareasize = 0;
	for (i=0; i<50; i++) {
		printf ("Size of area %d: %d blocks\n", i, areasizes[i]);
		// and keep track of the largest
		if (areasizes[i] > largestareasize) {
			largestarea = i;
			largestareasize = areasizes[i];
		}
	}
	// report the largest
	printf ("\nThe area with the largest size was area %d, with a size of %d\n", largestarea, largestareasize);

	outfile = fopen("day6a.pgm", "w");
	fprintf (outfile, "P2\n%d\n%d\n%d\n", XMAX, YMAX, 51);
		for (y=0; y<YMAX; y++) {
			for (x=0; x<XMAX; x++) {
			fprintf(outfile, "%d ", grid[x][y]);
		}
		fprintf(outfile, "\n");
	}
	fclose(outfile);
}
		
	
