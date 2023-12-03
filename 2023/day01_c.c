#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "day01.txt"

int get_calibration_value(char *line, int part_two) {
	char * line_ptr;
	char * line_end = line + strlen(line);
	int firstnum, lastnum, calibration_value, OK = 0;
	char * const numbernames[] = {"zero", "one", "two", "three", "four", "five", "six",
		"seven", "eight", "nine"};

	// strip
	if (*--line_end != '\n') {
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
		if (part_two) {
			for (int i = 0; i < 10; i++) {
				char *numbername = numbernames[i];
				int numbernamelen = strlen(numbername);
				if (line_ptr + numbernamelen > line_end + 1) continue;
				if (strncmp(line_ptr, numbername, numbernamelen) == 0) {
					firstnum = i;
					OK++;
					break;
				}
			}
			if (OK) break;
		}
	}

	// we shouldn't have reached the end of line without finding a number
	if (!OK) {
		fprintf(stderr, "No digits found in line! [%s]\n", line);
		return 0;
	}
	OK = 0;

	// search backwards for last number
	for (line_ptr = line_end; line_ptr >= line; line_ptr--) {
		if (*line_ptr >= '0' && *line_ptr <= '9') {
			lastnum = *line_ptr - '0';
			OK++;
			break;
		}
		if (part_two) {
			for (int i = 0; i < 10; i++) {
				char *numbername = numbernames[i];
				int numbernamelen = strlen(numbername);
				if (line_ptr + numbernamelen > line_end + 1) continue;
				if (strncmp(line_ptr, numbername, numbernamelen) == 0) {
					lastnum = i;
					OK++;
					break;
				}
			}
			if (OK) break;
		}
	}

	calibration_value = (firstnum * 10) + lastnum;
	// printf("Line: %s, calibration vaue: %d\n", line, calibration_value);
	return calibration_value;
}

void solve(FILE *infile, int part_two) {
	char *linebuf;
	linebuf = malloc(LINE_MAX);
	int running_total = 0;
	while (fgets(linebuf, LINE_MAX, infile) != NULL) {
		running_total += get_calibration_value(linebuf, part_two);
	}
	printf("Total is %d\n", running_total);
	free(linebuf);
}

void solve_pt1(FILE *infile) {
	solve(infile, 0);
}

void solve_pt2(FILE *infile) {
	solve(infile, 1);
}

int main(int argc, char **argv) {
	FILE *infile;
	infile = fopen(FILENAME, "r");

	printf("Part 1\n------\n");
	solve_pt1(infile);
	rewind(infile);
	printf("\nPart 2\n------\n");
	solve_pt2(infile);
	
	fclose(infile);
}
