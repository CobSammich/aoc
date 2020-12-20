#include <iostream>
#include <fstream>
#include <vector>

std::vector<std::vector<bool>> formTreeField(std::string filename) {
    // open file
    std::ifstream file(filename);
    // vector to store values
    std::vector<std::vector<bool>> treeField;
    std::string row;
    int rowNum = 0;
    while (getline(file, row)) {
        int size = row.size();
        std::vector<bool> treeRow;
        for (int i=0; i<size; ++i) {
            if (row[i] == '#') {
                treeRow.push_back(true);
            }
            else if (row[i] == '.') {
                treeRow.push_back(false);
            }
        }
        treeField.push_back(treeRow);
        rowNum++;
    }
    file.close();
    return treeField;
}

void printTreeField(std::vector<std::vector<bool>> treeField) {
    // Given a 2D tree field, print in terms of 0's and 1's
    // 1 means there is a tree, 0 means no tree.
    for (int i=0; i<treeField.size(); ++i) {
        std::vector<bool> row = treeField[i];
        for (int j=0; j<row.size(); ++j) {
            std::cout << row[j] << ' ';
        }
        std::cout << std::endl;
    }
}

int treesInPath(std::vector<std::vector<bool>> treeField,
                int columnIncrement, int rowIncrement) {
    int fieldHeight = treeField.size();
    int fieldWidth = treeField[0].size();

    int numTreesEncountered = 0;
    int column = 0;
    for (int row=0; row < fieldHeight; row += rowIncrement) {
        //printf("%d, %d\n", row, column);
        if (treeField[row][column] == 1) {
            numTreesEncountered++;
        }
        column += columnIncrement;
        column %= fieldWidth;
    }
    return numTreesEncountered;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Please specify input file\n");
        return -1;
    }
    std::string filename = argv[1];
    std::vector<std::vector<bool>> treeField = formTreeField(filename);
    // right moves
    int right[5] = {1, 3, 5, 7, 1};
    // corresponding down moves
    int down[5] = {1, 1, 1, 1, 2};
    int arrLength = sizeof(right) / sizeof(right[0]);
    printf("Size of array: %d\n", arrLength);

    int numTrees;
    uint64_t product = 1;
    for (int i=0; i < arrLength; ++i) {
        numTrees = treesInPath(treeField, right[i], down[i]);
        printf("Case %d: %d\n", i+1, numTrees);
        product *= numTrees;
    }
    std::cout << "Answer: " << product << std::endl;

    return 0;
}
