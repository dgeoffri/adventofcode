#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Car {
	int x, y, dir, nextTurn;     // Dir:  0=up  1=right  2=down  3=left   NextTurn:  0=left  1=straight  2=right
	struct Car * nextCar;	
};

struct Car * newCar(int dir, int nextTurn, struct Car * oldCar) {
	struct Car * newcar;
	newcar = malloc(sizeof(struct Car));
	newcar -> dir = dir;
	newcar -> nextTurn = nextTurn;
	newcar -> nextCar = oldCar;
	return newcar;
}

void marchCars(struct Car * carsHead, char grid[150][151]) {
	struct Car * car = carsHead;
	while (car != NULL) {
		switch (car->dir) {
			case 0:
				car->y--;
				break;
			case 1:
				car->x++;
				break;
			case 2:
				car->y++;
				break;
			case 3:
				car->x--;
				break;
		}
		switch (grid[car->y][car->x]) {                         // Dir:  0=up  1=right  2=down  3=left   NextTurn:  0=left  1=straight  2=right
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
		car = car->nextCar;
	}
}

void showCars(struct Car * carsHead) {
	struct Car * car;
	int i;
	car = carsHead;
	i = 0;
	while (car != NULL) {
		switch (car->dir) {
			case 0:
				printf ("Car %d has location (%d, %d) and faces up\n", i++, car->x, car->y);
				break;
			case 1:
				printf ("Car %d has location (%d, %d) and faces right\n", i++, car->x, car->y);
				break;
			case 2:
				printf ("Car %d has location (%d, %d) and faces down\n", i++, car->x, car->y);
				break;
			case 3:
				printf ("Car %d has location (%d, %d) and faces left\n", i++, car->x, car->y);
				break;
		}
		car = car->nextCar;
	}
	printf ("\n");
}

struct Car * plotCars(struct Car * carsHead, char grid[150][151]) {
	struct Car * car;
	struct Car * crashedCar = NULL;
	car = carsHead;
	while ((car != NULL) && (crashedCar == NULL)) {
		switch (grid[car->y][car->x]) {
			case '^':
			case '>':
			case 'v':
			case '<':
				crashedCar = car;
				grid[car->y][car->x] = 'X';
				break;
				
			default:
				switch (car->dir) {
					case 0:
						grid[car->y][car->x] = '^';
						break;
					case 1:
						grid[car->y][car->x] = '>';
						break;
					case 2:
						grid[car->y][car->x] = 'v';
						break;
					case 3:
						grid[car->y][car->x] = '<';
						break;
				}
				break;
		}
		car = car->nextCar;
	}
	return (crashedCar);
}

int main(int argc, char **argv) {
	FILE	*infile;
	char	grid[150][151];
	struct Car * cargrid[150][151];
	char	destgrid[150][151];
	struct Car * car = NULL;
	struct Car * crashedCar = NULL;
	int	x, y, i;

	infile = fopen("day13.txt", "r");
	fread (grid, 150, 151, infile);

	for (y=0; y<150; y++) {
		for (x=0; x<150; x++) {
			switch (grid[y][x]) {
				case '^':
					grid[y][x] = '|';
					cargrid[y][x] = nweCar(0, 0, cargrid[y][x]);
					break;
				case '>':
					grid[y][x] = '-';
					cargrid[y][x] = nweCar(1, 0, cargrid[y][x]);
					break;
				case 'v':
					grid[y][x] = '|';
					cargrid[y][x] = nweCar(2, 0, cargrid[y][x]);
					break;
				case '<':
					grid[y][x] = '-';
					cargrid[y][x] = nweCar(3, 0, cargrid[y][x]);
					break;
				case default:
					cargrid[y][x] = NULL;
					break;
			}
		}
		grid[y][150] = 0;
	}

	memcpy (destgrid, grid, sizeof(grid));
	while ((crashedCar=plotCars(carsHead, destgrid)) == NULL) {
		marchCars(carsHead, grid);
		memcpy (destgrid, grid, sizeof(grid));
	}

	printf("Crash!  Two carts collided at %d,%d\n", crashedCar->x, crashedCar->y);
	showCars(carsHead);
	plotCars(carsHead, destgrid);
	for (y=0; y<150; y++)
		printf ("%s\n", destgrid[y]);

	car = carsHead;
	while (car != NULL) {
		struct Car * oldcar = car;
		car = car->nextCar;
		free(oldcar);
	}
}
