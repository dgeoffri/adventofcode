#include <stdio.h>

#define XMAX     300
#define YMAX     300
#define GRIDSER  5468

int hundredsplace(int c) {
	return ((abs(c)%1000-abs(c)%100)/100);
}

int sum3x3(int grid[XMAX][YMAX], int startx, int starty) {
	int sum = 0, x, y;
	for (y=starty; y<starty+3 && y<YMAX; y++)
		for (x=startx; x<startx+3 && x<XMAX; x++)
			sum += grid[x][y];
	return sum;
}

struct Winner {
	int x, y, score;
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

	struct Winner winner = { 0, 0, grid[0][0] };
	for (y=0; y<(YMAX-3); y++)
		for (x=0; x<(XMAX-3); x++)
			if (sum3x3(grid, x, y) > winner.score) {
				winner.x = x;
				winner.y = y;
				winner.score = sum3x3(grid, x, y);
			}
	
	printf ("The 3x3 grid with the highest score starts at (%d, %d) with a score of %d\n", winner.x+1, winner.y+1, winner.score);
}
