#include <iostream>
#include <fstream>
#include <vector>

std::vector<int> readFileContents(std::string filename) {
    // open file
    std::ifstream file;
    file.open(filename);
    // vector to store values
    std::vector<int> fileContents;
    std::string text;
    while (getline(file, text)) {
        int val = std::stoi(text);
        fileContents.push_back(val);
    }
    file.close();
    return fileContents;
}

void printVector(std::vector<int> v) {
    // TODO how to print values of any vector?
    for (int i=0; i< v.size(); ++i) {
        std::cout << v[i] << std::endl;
    }
}

int find2020(std::vector<int> v) {
    // O(nlogn) ??
    // two entries that sum to 2020, multiply them together
    for (int i=0; i < v.size(); ++i) {
        for (int j=i; j < v.size(); ++j) {
            for (int k=j; k < v.size(); ++k) {
                int D = 2028 - (v[i] + v[j] + v[k]);
                if (8==D) {
                    printf("%d, %d, %d\n", v[i], v[j], v[k]);
                    return v[i] * v[j] * v[k];
                }
            }
        }
    }
    return -1;
}
int main(int argc, char* argv[]) {
    //int nLines = getNumLinesInFile("data/test.txt");
    std::vector<int> fileContents = readFileContents("data/puzzle.txt");

    printVector(fileContents);

    printf("Finding the two values that sum to 2020...\n");
    int product = find2020(fileContents);
    printf("Answer: %d\n", product);

    return 0;
}

