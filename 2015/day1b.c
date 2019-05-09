#include <stdio.h>

int main(int argc, char **argv) {
	char * dir;
	int floor = 0;
	int no_basement = 1;
	if (argc != 2) {
		printf ("Please provide your puzzle input as the first argument\n");
		return 1;
	}
	dir = argv[1];
	while (*dir) {
		switch (*dir++) {
			case '(':
				floor++;
				break;
			case ')':
				floor--;
		}
		if ((floor < 0) && no_basement) {
			printf ("Santa arrived in the basement at position %d\n", (int) (dir-argv[1]));
			no_basement = 0;
		}
	}
	printf ("Santa should arrive on floor %d\n", floor);
}
