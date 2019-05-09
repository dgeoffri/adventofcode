#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Coord {
	int x;
	int y;
};

struct Car {
	int x, y, dir, nextTurn;     // Dir:  0=up  1=right  2=down  3=left   NextTurn:  0=left  1=straight  2=right
	struct Car * nextCar;
	int alreadyMoved;
};

struct Car * newCar(int dir, int nextTurn, struct Car * oldCar) {
	struct Car * newcar;
	newcar = malloc(sizeof(struct Car));
	newcar -> dir = dir;
	newcar -> nextTurn = nextTurn;
	newcar -> nextCar = oldCar;
	return newcar;
}

int marchCars(struct Car * cargrid[150][151], char grid[150][151]) {
	struct Car * car;
	int x, y, carsLeft = 0;
	for (y=0; y<150; y++)
		for (x=0; x<150; x++)
			if (cargrid[y][x]) {
				cargrid[y][x]->alreadyMoved = 0;
				carsLeft++;
			}
	for (y=0; y<150; y++)
		for (x=0; x<150; x++) {
			if ((cargrid[y][x]) && !(cargrid[y][x]->alreadyMoved)) {
				car = cargrid[y][x];
				int xnew = x, ynew = y;
				switch (car->dir) {
					case 0:
						ynew--;
						break;
					case 1:
						xnew++;
						break;
					case 2:
						ynew++;
						break;
					case 3:
						xnew--;
						break;
				}
				if (cargrid[ynew][xnew]) {
					free(car);
					free(cargrid[ynew][xnew]);
					cargrid[y][x] = NULL;
					cargrid[ynew][xnew] = NULL;
					carsLeft -= 2;
				} else {
					cargrid[ynew][xnew] = cargrid[y][x];
					cargrid[y][x] = NULL;
				}
				switch (grid[ynew][xnew]) {                // Dir:  0=up  1=right  2=down  3=left   NextTurn:  0=left  1=straight  2=right
					case '/':
						switch (car->dir) {
							case 0:
								car->dir = 1;
								break;
							case 1:
								car->dir = 0;
								break;
							case 2:
								car->dir = 3;
								break;
							case 3:
								car->dir = 2;
								break;
						}
						break;
					case '\\':
						switch (car->dir) {
							case 0:
								car->dir = 3;
								break;
							case 1:
								car->dir = 2;
								break;
							case 2:
								car->dir = 1;
								break;
							case 3:
								car->dir = 0;
								break;
						}
						break;
					case '+':                         // Dir:  0=up  1=right  2=down  3=left   NextTurn:  0=left  1=straight  2=right
						switch (car->nextTurn) {
							case 0:
								switch (car->dir) {
									case 0:
										car->dir = 3;
										break;
									case 1:
										car->dir = 0;
										break;
									case 2:
										car->dir = 1;
										break;
									case 3:
										car->dir = 2;
										break;
								}
								break;
							case 2:
								switch (car->dir) {
									case 0:
										car->dir = 1;
										break;
									case 1:
										car->dir = 2;
										break;
									case 2:
										car->dir = 3;
										break;
									case 3:
										car->dir = 0;
										break;
								}
								break;
							break;
						}
						car->nextTurn++;
						car->nextTurn %= 3;
						break;
				}
				car->alreadyMoved = 1;
			}
		}
	return carsLeft;
}

void showCars(struct Car * cargrid[150][151]) {
	struct Car * car;
	int x, y;
	int i = 0;
	for (y=0; y<150; y++)
		for (x=0; x<150; x++) {
			car = cargrid[y][x];
			if (car) {
				switch (car->dir) {
					case 0:
						printf ("Car %d has location (%d, %d) and faces up\n", i++, x, y);
						break;
					case 1:
						printf ("Car %d has location (%d, %d) and faces right\n", i++, x, y);
						break;
					case 2:
						printf ("Car %d has location (%d, %d) and faces down\n", i++, x, y);
						break;
					case 3:
						printf ("Car %d has location (%d, %d) and faces left\n", i++, x, y);
						break;
				}
			}
		}
	printf ("\n");
}

void plotCars(struct Car * cargrid[150][151], char grid[150][151]) {
	struct Car * car;
	int x, y;
	for (y=0; y<150; y++)
		for (x=0; x<150; x++) {
			car = cargrid[y][x];
			if (car) {
				switch (car->dir) {
					case 0:
						grid[y][x] = '^';
						break;
					case 1:
						grid[y][x] = '>';
						break;
					case 2:
						grid[y][x] = 'v';
						break;
					case 3:
						grid[y][x] = '<';
						break;
				}
			}
		}
}

int main(int argc, char **argv) {
	FILE		*infile;
	FILE		*outfile;
	char		outfilename[64];
	struct Car * 	cargrid[150][151];
	char		grid[150][151];
	char		destgrid[150][151];
	struct Car * 	car = NULL;
	struct Coord * 	collisionPoint;
	int		x, y, i = 0, carsLeft;

	infile = fopen("day13.txt", "r");
	fread (grid, 150, 151, infile);
	fclose (infile);

	for (y=0; y<150; y++) {
		for (x=0; x<150; x++) {
			switch (grid[y][x]) {
				case '^':
					grid[y][x] = '|';
					cargrid[y][x] = newCar(0, 0, cargrid[y][x]);
					break;
				case '>':
					grid[y][x] = '-';
					cargrid[y][x] = newCar(1, 0, cargrid[y][x]);
					break;
				case 'v':
					grid[y][x] = '|';
					cargrid[y][x] = newCar(2, 0, cargrid[y][x]);
					break;
				case '<':
					grid[y][x] = '-';
					cargrid[y][x] = newCar(3, 0, cargrid[y][x]);
					break;
				default:
					cargrid[y][x] = NULL;
					break;
			}
		}
		grid[y][150] = 0;
	}

	// memcpy (destgrid, grid, sizeof(grid));
	// while ((crashedCar=plotCars(carsHead, destgrid)) == NULL) {
	//	marchCars(carsHead, grid);
	//	memcpy (destgrid, grid, sizeof(grid));
	// }
	while ((carsLeft = marchCars(cargrid, grid))>1) {
		// showCars(cargrid);
		memcpy (destgrid, grid, sizeof(grid));
		plotCars(cargrid, destgrid);
		snprintf(outfilename, sizeof(outfilename), "day13b-frame%08d.txt", i++);
		outfile = fopen(outfilename, "w");
		for (y=0; y<150; y++)
			fprintf (outfile, "%s\n", destgrid[y]);
		fclose (outfile);
		showCars(cargrid);
	}
	for (y=0; y<150; y++)
		for (x=0; x<150; x++)
			if (cargrid[y][x])
				printf ("Last car is at %d,%d!\n", x, y);
}
