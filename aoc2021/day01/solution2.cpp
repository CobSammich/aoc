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
int timesIncreasedSlidingWindow(const std::vector<int>& depths, int k = 3) {
    int nTimesIncreased = 0;

    // get the first sliding window sum
    int lastValue = 0;
    for (int i = 0; i < k; ++i)
        lastValue += depths[i];
    printf("%d (N/A - no previous sum)\n", lastValue);


    for (int i = 1; i < depths.size() - k + 1; ++i) {
        int currValue = 0;
        for (int j = 0; j < k; ++j) {
            currValue += depths[i + j];
        }

        if (currValue > lastValue) {
            nTimesIncreased++;
            printf("%d (increased)\n", currValue);
        }
        else
            printf("%d (decreased)\n", currValue);
        lastValue = currValue;
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

    int answer = timesIncreasedSlidingWindow(depths);
    printf("Answer: %d\n", answer);

    return 0;
}
