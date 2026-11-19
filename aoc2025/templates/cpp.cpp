#include <iostream>
#include <fstream>
#include <vector>

std::vector<int> readInputFile(const std::string& filename) {
    std::vector<int> values;

    std::ifstream infile(filename);
    int value;

    while (infile >> value) {
        values.push_back(value);
    }
    return values;
}


int main (int argc, char *argv[]) {


  return 0;
}
