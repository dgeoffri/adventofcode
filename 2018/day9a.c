#include <stdio.h>
#include <stdlib.h>

#define HIGHESTMARBLE 71240
#define NUMELVES 478

struct Marble {
	int value;
	struct Marble *lastMarble;
	struct Marble *nextMarble;
};

struct Marble * insertMarble(struct Marble *currentMarble, struct Marble *newMarble) {
	newMarble->lastMarble = currentMarble->nextMarble;
	newMarble->nextMarble = currentMarble->nextMarble->nextMarble;
	currentMarble->nextMarble->nextMarble->lastMarble = newMarble;
	currentMarble->nextMarble->nextMarble = newMarble;
	return newMarble;
}

struct Marble * removeMarble(struct Marble *currentMarble) {
	currentMarble = currentMarble->lastMarble->lastMarble->lastMarble->lastMarble->lastMarble->lastMarble->lastMarble;
	currentMarble->lastMarble->nextMarble = currentMarble->nextMarble;
	currentMarble->nextMarble->lastMarble = currentMarble->lastMarble;
	return currentMarble;
}

void showAllMarbles(char *e, struct Marble *headMarble, struct Marble *currentMarble) {
	struct Marble *ptr;
	ptr = headMarble;
	printf ("[%s]", e);
	do {
		if (ptr == currentMarble)
			printf (" (%d)", ptr->value);
		else
			printf (" %d", ptr->value);
		// ptr = ptr->nextMarble;
		ptr = ptr->lastMarble;
	} while (ptr != headMarble);
	putchar ('\n');
}

int main(int argc, char **argv) {
	struct Marble *currentMarble;
	struct Marble *headMarble;

	struct Marble *elfMarbles[NUMELVES] = { NULL };

	int i;
	int currentElf=0;
	char elfnum[10];

	struct Marble *marbles = calloc(sizeof(struct Marble), HIGHESTMARBLE+1);

	if (NULL == marbles) {
		fprintf(stderr, "Could not allocate dynamic memory for marbles, aborting!\n");
		exit(1);
	}

	for (i=1; i<=HIGHESTMARBLE; i++) {
		marbles[i].value = i;
		marbles[i].lastMarble = NULL;
		marbles[i].nextMarble = NULL;
	}

	marbles[0].value = 0;
	marbles[0].lastMarble = &marbles[0];
	marbles[0].nextMarble = &marbles[0];
	
	headMarble = &marbles[0];
	currentMarble = headMarble;

	// showAllMarbles("-", headMarble, currentMarble);

	for (i=1; i<=HIGHESTMARBLE; i++) {
		if (i % 23)
			currentMarble = insertMarble(currentMarble, &marbles[i]);
		else {
			struct Marble * tmpMarble;
			tmpMarble = &marbles[i];
			tmpMarble->nextMarble = elfMarbles[currentElf];
			elfMarbles[currentElf] = tmpMarble;

			tmpMarble = removeMarble(currentMarble);
			currentMarble = tmpMarble->nextMarble;
			tmpMarble->nextMarble = elfMarbles[currentElf];
			elfMarbles[currentElf] = tmpMarble;
		}
#ifdef DEBUG
		snprintf (elfnum, sizeof(elfnum), "%d", currentElf+1);
		// showAllMarbles(elfnum, headMarble, currentMarble);
#endif
	
		currentElf++;
		if (currentElf >= NUMELVES)
			currentElf = 0;
	}

	unsigned int highScore = 0;
	for (i=0; i < NUMELVES; i++) {
		struct Marble * tmpMarble;
		unsigned int elfScore = 0;
		tmpMarble = elfMarbles[i];
		while (tmpMarble != NULL) {
			// printf (" %d", tmpMarble->value);
			elfScore += tmpMarble->value;
			tmpMarble = tmpMarble->nextMarble;
		}
		// printf (" total: %u\n", elfScore);
		if (elfScore > highScore)
			highScore = elfScore;
	}
	free(marbles);
	printf ("The highest score awarded was: %u\n", highScore);
}
