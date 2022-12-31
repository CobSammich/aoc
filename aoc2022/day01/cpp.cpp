#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

std::vector<int> readInput(const std::string& filename) {
    std::vector<int> elves;

    std::ifstream infile(filename);
    int currBuffer = 0;
    for (std::string currLine; std::getline(infile, currLine);) {
        if (currLine.empty()) {
            elves.push_back(currBuffer);
            currBuffer = 0;
            continue;
        }
        // Convert to int
        currBuffer +=  std::stoi(currLine);
    }
    return elves;
}


int part1(std::vector<int> data) {
    if (data.empty())
        return -1;
    int max = data.front();
    for (int val: data) {
        if (val > max)
            max = val;
    }
    return max;
}


int part2(std::vector<int> data, int n) {
    if (data.empty())
        return -1;

    std::sort(data.begin(), data.end(), std::greater<int>());
    int sum = 0;
    for (int i = 0; i < n; ++i)
        sum += data[i];
    return sum;
}


int main (int argc, char *argv[]) {

    if (argc < 2) {
        printf("Please enter filename as input.\n");
        return -1;
    }

    std::string filename = argv[1];

    std::vector<int> elves = readInput(filename);

    int p1 = part1(elves);
    printf("Part 1: %d\n", p1);
    int p2 = part2(elves, 3);
    printf("Part 2: %d\n", p2);

    return 0;
}
