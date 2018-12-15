#include <stdio.h>
#include <string.h>
#include <unistd.h>

#ifndef MAXGENERATIONS
  #define MAXGENERATIONS 200
#endif

int checkall(char *cmpstart, const char **patterns) {
	int matched = 0;
	do {
		// printf("Checking %s\n", *patterns);
		if (strncmp(*patterns, cmpstart, 5) == 0) {
			matched = 1;
			// printf ("Matched %s\n", *patterns);
			break;
		}
	} while (*++patterns != NULL); 
	return matched;
}

int main(int argc, char **argv) {
	const char *patterns[] = { 
		"##..#",
		"..#.#",
		".##..",
		"##...",
		"#..##",
		".###.",
		".##.#",
		"##.#.",
		"#.#..",
		".#...",
		"...#.",
		NULL };

	char startstring[] = "#..######..#....#####..###.##..#######.####...####.##..#....#.##.....########.#...#.####........#.#.";
	char initialstate[3000];
	char deststate[sizeof(initialstate)];
	char *srcptr;
	char *dstptr;
	int i, j;

	memset (initialstate, '.', sizeof(initialstate));
	memset (deststate, '.', sizeof(deststate));
	memcpy (initialstate+100, startstring, sizeof(startstring)-1);

	srcptr = initialstate;	
	for (i=0; i<sizeof(initialstate); i++)
		putchar (*srcptr++);
	putchar('\n');

	for (j=0; j<MAXGENERATIONS; j++) {
		srcptr = initialstate;
		dstptr = deststate + 2;
		for (i=0; i<sizeof(initialstate)-5; i++)
			if (checkall(srcptr++, patterns))
				*dstptr++ = '#';
			else
				*dstptr++ = '.';
		// printf("%d\n", j);
		srcptr = deststate;	
		for (i=0; i<sizeof(deststate); i++)
			putchar (*srcptr++);
		printf("\033[2J\033[H");
		usleep(3000);

		memcpy (initialstate, deststate, sizeof(deststate));
	}

	long long potnumber = 50000000000-100-MAXGENERATIONS, sum = 0;
	srcptr = deststate;
	for (i=0; i<sizeof(deststate); i++)
		if (*srcptr++ == '#')
			sum += (potnumber + i);
	printf ("Sum: %lld\n", sum);
}
