#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

/**
 * @brief Reads integer values line by line from a file and pushes them onto a vector, then returns
 * the vector
 *
 * @param filename the filename to read from
 */
std::vector<int> readInputFile(const std::string& filename) {
    std::vector<int> depths;

    std::ifstream infile(filename);
    int value;
    while (infile >> value) {
        depths.push_back(value);
    }
    return depths;
}

/**
 * @brief Counts the number of times each value in this depths vector increases from the previous
 * value
 *
 * @param depths - vector of ints containing the depths to check for increasing values.
 * @return The number of times the value increased from the previous value in the vector
 */
int timesIncreased(const std::vector<int>& depths) {
    int nTimesIncreased = 0;

    // get the first value
    int lastValue = depths.at(0);

    for (int i = 1; i < depths.size(); ++i) {
        if (depths[i] > lastValue) {
            nTimesIncreased++;
            printf("%d (increased)\n", depths[i]);
        }
        else
            printf("%d (decreased)\n", depths[i]);
        lastValue = depths[i];
    }
    return nTimesIncreased;
}

int main (int argc, char *argv[]) {

    if (argc != 2) {
        std::cout << "Enter a filename to read, dingus" << std::endl;
        return -1;
    }

    std::string filename = argv[1];
    // does the file actually exist
    if (!std::filesystem::exists(filename))
        std::cout << "Please enter a valid filename. " << filename << " does not exist"
            << std::endl;

    std::vector<int> depths = readInputFile(filename);

    int answer = timesIncreased(depths);
    printf("Answer: %d\n", answer);

    return 0;
}
