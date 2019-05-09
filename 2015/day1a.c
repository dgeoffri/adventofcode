#include <stdio.h>

int main(int argc, char **argv) {
	char * dir;
	int floor = 0;
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
	}
	printf ("Santa should arrive on floor %d\n", floor);
}
