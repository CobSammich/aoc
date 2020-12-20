#include <iostream>
#include <fstream>
#include <algorithm>

struct PasswordContainer {
    int position1;
    int position2;
    char mainChar;
    std::string password;
};

int charToFuckingInt(char c) {
    return c - '0';
}

bool isPasswordValid (PasswordContainer *pc) {
    int numberOfOccurences = std::count(pc->password.begin(), pc->password.end(), pc->mainChar);

    // check spot 1
    bool spot1 = pc->mainChar == pc->password[pc->position1-1];
    // check spot 2
    bool spot2 = pc->mainChar == pc->password[pc->position2-1];

    // XOR
    if (spot1 ^= spot2) {
        return true;
    }
    //printf("%d, %d, %c, %s\n", pc->position1, pc->position2, pc->mainChar, pc->password.c_str());
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
        // scan in the range from the given format
        std::sscanf(range.c_str(), "%d-%d", &current.position1, &current.position2);
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

