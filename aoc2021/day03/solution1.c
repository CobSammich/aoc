#include <stdbool.h>
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
int getDataSizeY(char *filename) {
    FILE *fp = fopen(filename, "r");
    // file could not be read
    if (fp == NULL) {
        printf("File could not be read.\n");
        return -1;
    }

    // iterate over file and return the number of pieces of data
    int nLines = 0;
    while (!feof(fp)) {
        char ch = fgetc(fp);
        if (ch == '\n') {
            nLines++;
        }
    }
    fclose(fp);
    return nLines;
}

int getDataSizeX(char *filename) {
    FILE *fp = fopen(filename, "r");
    // file could not be read
    if (fp == NULL) {
        printf("File could not be read.\n");
        return -1;
    }

    char *line = NULL;
    size_t nBytes;
    int line_size = getline(&line, &nBytes, fp);
    // line includes '\n'
    return line_size - 1;
}

bool charToBit(const char c) { return c == '1'; }

int readInput(char *filename, bool *bits[], int xLength, int yLength) {
    printf("%d\n", bits[0][0]);
    FILE *fp = fopen(filename, "r");
    // file could not be read
    if (fp == NULL) {
        printf("File could not be read.\n");
        return -1;
    }

    printf("%d\n", bits[0][0]);
    char bit = ' ';
    for (int row = 0; row < yLength; row++) {
        for (int col = 0; col < xLength; col++) {
            printf("%d\n", bits[row][col]);
            fscanf(fp, "%c", &bit);
            bits[row][col] = charToBit(bit);
            printf("%d\n", bits[row][col]);
        }
    }
    return 0;
}

int solve(struct Command *commands) {
    int nCommands = commands[0].length;

    // keep track of positions
    int xPos = 0;
    int yPos = 0;

    for (int i = 0; i < nCommands; i++) {
        struct Command currCommand = commands[i + 1];
        char *currDirection = currCommand.direction;
        int currLength = currCommand.length;
        if (strcmp(currDirection, "forward") == 0) {
            xPos += currLength;
        }
        else if (strcmp(currDirection, "down") == 0) {
            yPos += currLength;
        }
        else if (strcmp(currDirection, "up") == 0) {
            yPos -= currLength;
        }
    }
    return xPos * yPos;
}

int main(int argc, char **argv) {
    // get number of ints in file
    printf("%s\n", argv[1]);
    // int nData = getSizeOfData(argv[1]);
    int xLength = getDataSizeX(argv[1]);
    int yLength = getDataSizeY(argv[1]);

    printf("bit matrix is size: %dx%d\n", xLength, yLength);

    // Initialize a 2D bit array to zero
    bool bits[yLength][xLength];
    memset(bits, 0, xLength * yLength * sizeof(bool));

    // first item in this list is the length of the array
    // struct Command commands[nData + 1];
    // struct Command metadata;
    // make length of commands first entry
    // strcpy(metadata.direction, "ArrayLen");
    // metadata.length = nData;
    // commands[0] = metadata;

    readInput(argv[1], &bits, xLength, yLength);

    // int answer = solve(commands);
    // printf("The answer is %d\n", answer);

    return 0;
}
