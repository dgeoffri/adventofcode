#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "day01.txt"

int get_calibration_value_pt1(char *line) {
	char * line_ptr;
	char * line_end = line + strlen(line);
	int firstnum, lastnum, calibration_value, OK = 0;

	// strip
	if (*--line_end != '\n') {
		printf("%s\n", line);
		fprintf(stderr, "Bad dragons! %d", *line_end);
		exit(2);
	}
	*line_end-- = '\0';

	// search forwards for first number
	for (line_ptr = line; line_ptr <= line_end; line_ptr++) {
		if (*line_ptr >= '0' && *line_ptr <= '9') {
			firstnum = *line_ptr - '0';
			OK++;
			break;
		}
	}

	// we shouldn't have reached the end of line without finding a number
	if (!OK) {
		fprintf(stderr, "No digits found in line! [%s]\n", line);
		return 0;
	}

	// search backwards for last number
	for (line_ptr = line_end; line_ptr >= line; line_ptr--) {
		if (*line_ptr >= '0' && *line_ptr <= '9') {
			lastnum = *line_ptr - '0';
			break;
		}
	}

	calibration_value = (firstnum * 10) + lastnum;
	printf("Line: %s, calibration vaue: %d\n", line, calibration_value);
	return calibration_value;
}

void solve_pt1(FILE *infile) {
	char linebuf[128];
	// linebuf = malloc(LINE_MAX);
	long int running_total = 0;
	while (fgets(linebuf, sizeof(linebuf), infile) != NULL) {
		running_total += get_calibration_value_pt1(linebuf);
	}
	printf("Total is %ld\n", running_total);
	// free(linebuf);
}

void solve_pt2(FILE *infile) {
	printf("Not yet implemented!\n");
}

int main(int argc, char **argv) {
	FILE *infile;
	infile = fopen(FILENAME, "r");

	printf("Part 1\n------\n");
	solve_pt1(infile);
	// rewind(infile);
	// printf("\nPart 2\n------\n");
	// solve_pt2(infile);
	
	fclose(infile);
}
