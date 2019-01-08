#include <stdio.h>
#include <stdlib.h>

#define XMAX     300
#define YMAX     300
#define GRIDSER  5468

int hundredsplace(int c) {
	return ((abs(c)%1000-abs(c)%100)/100);
}

int sumsquare(int grid[XMAX][YMAX], int startx, int starty, int size) {
	int sum = 0, x, y;
	for (y=starty; y<starty+size && y<YMAX; y++)
		for (x=startx; x<startx+size && x<XMAX; x++)
			sum += grid[x][y];
	return sum;
}

struct Winner {
	int x, y, size, score;
};

int main(int argc, char **argv) {
	int 		grid[XMAX][YMAX];
	int 		x, y, i;

	for (y=0; y<YMAX; y++)
		for (x=0; x<XMAX; x++) {
			int rackid = (x + 1) + 10;  // Rack ID is the cell's X-coordinate (1-based) plus 10
			int powerlevel = (rackid * (y+1)) + GRIDSER;
			powerlevel = hundredsplace(powerlevel*rackid)-5;
			grid[x][y] = powerlevel;	
		}

	struct Winner winner = { 0, 0, 1, grid[0][0] };
	for (i=1; i<300; i++)
		for (y=0; y<(YMAX-i); y++)
			for (x=0; x<(XMAX-i); x++)
				if (sumsquare(grid, x, y, i) > winner.score) {
					winner.x = x;
					winner.y = y;
					winner.size = i;
					winner.score = sumsquare(grid, x, y, i);
				}
	
	printf ("The grid with the highest score starts at (%d, %d), has a size of %dx%d, and a score of %d\n", winner.x+1, winner.y+1, winner.size, winner.size, winner.score);
}
