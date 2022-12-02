#include <iostream>
#include <fstream>
#include <algorithm>

struct PasswordContainer {
    int min;
    int max;
    char mainChar;
    std::string password;
};

int charToFuckingInt(char c) {
    return c - '0';
}

bool isPasswordValid (PasswordContainer *pc) {
    int numberOfOccurences = std::count(pc->password.begin(), pc->password.end(), pc->mainChar);
    if (numberOfOccurences >= pc->min && numberOfOccurences <= pc->max) {
        return true;
    }
    return false;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Please specify input file\n");
        return -1;
    }
    std::string filename = argv[1];
    std::ifstream file(filename);
    std::string range;
    std::string character;
    std::string passwd;

    int numValidPasswords = 0;
    while (file >> range >> character >> passwd) {
        // set up a password container
        PasswordContainer current;
        // Not accounting for double digit numbers... scan string into values
        std::sscanf(range.c_str(), "%d-%d", &current.min, &current.max);
        //current.min = charToFuckingInt(range[0]);
        //current.max = charToFuckingInt(range[2]);
        current.mainChar = character[0];
        current.password = passwd;
        // is the password valid?
        if (isPasswordValid(&current)) {
            numValidPasswords++;
        }
    }
        //std::cout << range[0] << ' ' << character << ' ' << passwd << ' ' << std::endl;
        printf("Number of valid passwords: %d\n", numValidPasswords);

    return 0;
}

