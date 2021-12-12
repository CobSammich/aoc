#include <stdio.h>

/**
  * This function reads the given file and determines how many relevant pieces of data are in it.
  * In this case, every line in the file contains 1 piece of data.
  */
int getSizeOfData(char* filename) {
    FILE* fp = fopen(filename, "r");
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

int readInput(char* filename, int* data) {
    FILE* fp = fopen(filename, "r");
    // file could not be read
    if (fp == NULL) {
        printf("File could not be read.\n");
        return -1;
    }

    int i = 1;
    int val;
    // read in data as an int
    while (fscanf(fp, "%d", &val) == 1) {
        printf("%d\n", val);
        data[i++] = val;
        //printf("i: %d, val: %d\n", i-1, data[i-1]);
    }
    return 0;
}

/**
  * Iterates over the data and counts the number of times it has increased.
  */
int timesIncreased(int* data) {
    // length of array is stored as metadata in the array
    int n = data[0];
    printf("Iterating over %d items\n", n);

    int n_increased = 0;
    // get initial value
    int last_val = data[1];
    for (int i = 2; i <= n; i++) {
        // check if we increased depth
        int curr_val = data[i];
        if (curr_val > last_val) {
            printf("%d > %d\n", curr_val, last_val);
            n_increased++;
        }
        last_val = curr_val;
    }
    return n_increased;
}


int main(int argc, char** argv) {
    // get number of ints in file
    int nData = getSizeOfData(argv[1]);
    printf("Number of lines in file: %d\n", nData);

    // first item in this list is the length of the array
    int data[nData + 1];
    data[0] = nData;

    readInput(argv[1], data);
    printf("%d\n", data[3]);

    int answer = timesIncreased(data);
    printf("The answer is %d\n", answer);

    return 0;
}

