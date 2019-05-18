#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void incrementPassword (char *password) {
	char *passwordEnd;
	bool carryFlag = true;
	passwordEnd = password + strnlen(password, 255) - 1;

	while (passwordEnd >= password) {
		if (carryFlag) {
			(*passwordEnd)++;
			if ((*passwordEnd) > 'z') {
				(*passwordEnd) = 'a';
				carryFlag = true;
			} else {
				carryFlag = false;
			}
		}
		--passwordEnd;
	}
}

bool validatePassword (char *password) {
	char *passwordEnd;
	char lastchar = '\0';
	int straightNeeded = 2;
	int doublesNeeded = 2;
	bool justDoubled = false;

	passwordEnd = password + strnlen(password, 255) - 1;
	while (password <= passwordEnd)	{
		switch (*password) {
			case 'i':
			case 'o':
			case 'l':
				return false;
		}
		if (straightNeeded) {
			if ((lastchar) && (*password == lastchar+1))
				--straightNeeded;
			else
				straightNeeded = 2;
		}
		if (!justDoubled && *password == lastchar) {
			--doublesNeeded;
			justDoubled = true;
		} else {
			justDoubled = false;
		}
		lastchar = *password++;
	}
	return (!straightNeeded && !doublesNeeded);
}

void setNextValidPassword (char *password) {
	do 
		incrementPassword(password); 
	while (!validatePassword(password));
}

int main (int argc, char **argv) {
	char password[255];

	if (argc < 2) {
		printf("Usage: %s <current password>\n\nReturns the next 2 valid passwords for Santa that follow his own rotation system and comply with the minimum password strength requirements\n",argv[0]);
		exit(1);
	}

	strncpy(password, argv[1], sizeof(password));
	password[sizeof(password)-1] = '\0';

	setNextValidPassword(password);
	printf("The next valid password for Santa is %s\n", password);

	setNextValidPassword(password);
	printf("The one after that is %s\n", password);
	exit(0);
}
