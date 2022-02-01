#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Command {
    char direction[10];
    int length;
};

/**
 * This function reads the given file and determines how many relevant pieces of
 * data are in it. In this case, every line in the file contains 1 piece of
 * data.
 */
int getSizeOfData(char *filename) {
    FILE *fp = fopen(filename, "r");
    // file could not be read
    if (fp == NULL) {
        printf("File could not be read.\n");
        return -1;
    }

    // iterate over file and return the number of pieces of data
    int nData = 0;
    while (!feof(fp)) {
        char ch = fgetc(fp);
        if (ch == '\n') {
            nData++;
        }
    }
    return nData;
}

int readInput(char *filename, struct Command *commands) {
    FILE *fp = fopen(filename, "r");
    // file could not be read
    if (fp == NULL) {
        printf("File could not be read.\n");
        return -1;
    }

    int i = 1;
    int length;
    char direction[10]; // = malloc(sizeof(char) * 10);
    printf("Reading file\n");
    // read in data as an int
    while (fscanf(fp, "%s %d", direction, &length) == 2) {
        printf("%s %d\n", direction, length);
        struct Command currCommand;
        currCommand.length = length;
        strcpy(currCommand.direction, direction);
        commands[i] = currCommand;
        i++;
    }
    return 0;
}

int solve(struct Command *commands) {
    int nCommands = commands[0].length;

    // keep track of positions
    int xPos = 0;
    int yPos = 0;
    int aim = 0;

    for (int i = 0; i < nCommands; i++) {
        // Get current command
        struct Command currCommand = commands[i + 1];
        char *currDirection = currCommand.direction;
        int currLength = currCommand.length;

        if (strcmp(currDirection, "forward") == 0) {
            xPos += currLength;
            yPos += currLength * aim;
        }
        else if (strcmp(currDirection, "down") == 0) {
            aim += currLength;
        }
        else if (strcmp(currDirection, "up") == 0) {
            aim -= currLength;
        }
    }
    return xPos * yPos;
}

int main(int argc, char **argv) {
    // get number of ints in file
    printf("%s\n", argv[1]);
    int nData = getSizeOfData(argv[1]);
    printf("Number of lines in file: %d\n", nData);

    // first item in this list is the length of the array
    struct Command commands[nData + 1];
    struct Command metadata;
    // make length of commands first entry
    strcpy(metadata.direction, "ArrayLen");
    metadata.length = nData;
    commands[0] = metadata;

    readInput(argv[1], commands);

    int answer = solve(commands);
    printf("The answer is %d\n", answer);

    return 0;
}
