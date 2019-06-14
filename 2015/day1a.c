#include <stdio.h>
#include <stdlib.h>

char * readfile(const char *fname) {
	FILE * f;
	size_t s, t;
	char * data;
	f = fopen(fname, "r");
	if (NULL == f) {
		fprintf(stderr, "There was an error opening the input file.  Aborting!\n");
		exit(1);
	}
	if (fseek(f, 0L, SEEK_END)) {
		fprintf(stderr, "Error seeking to end of file.  Aborting!\n");
		exit(1);
	}
	s = ftell(f);
	rewind(f);
	data = malloc(s+1);
	if (NULL == data) {
		fprintf(stderr, "Could not allocate memory for file.  Aborting!\n");
		exit(1);
	}
	t = fread(data, sizeof(char), s, f);
	if (t != s) {
		fprintf(stderr, "Could not read file.  Aborting!\n");
		exit(1);
	}
	data[t+1] = '\0';
	return(data);
}

int main(int argc, char **argv) {
	char * filedata, * dir;
	int floor = 0;
	if (argc != 2) {
		printf ("Please provide the filename containing your puzzle input as the first argument\n");
		return 1;
	}
	filedata = readfile(argv[1]);
	dir = filedata;
	while (*dir) {
		switch (*dir++) {
			case '(':
				floor++;
				break;
			case ')':
				floor--;
		}
	}
	free(filedata);
	printf ("Santa should arrive on floor %d\n", floor);
}
