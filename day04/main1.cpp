#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

/*
 * There are 8 fields per record. The only field that can be empty is the
 * "cid" field. So, there are 3? cases
 * 1. All 8 fields are present: Valid
 * 2. cid is not present but all others are: Valid
 * 3. cid is not present and 1-6 other fields are present: Invalid
 * 4. cid is present, but another field is not: Invalid
 */

struct Record {
    std::string byr = ""; // Birth year
    std::string iyr = ""; // Issue year
    std::string eyr = ""; // Expiration year
    std::string hgt = ""; // Height
    std::string hcl = ""; // Hair color
    std::string ecl = ""; // Eye color
    std::string pid = ""; // Passport ID
    std::string cid = ""; // country ID

    void clearRecord() {
        byr = "";
        iyr = "";
        eyr = "";
        hgt = "";
        hcl = "";
        ecl = "";
        pid = "";
        cid = "";
    }
};

std::vector<Record> readRecordFile(std::string filename) {
    // open file
    std::ifstream file(filename);
    // return value -- array of records
    std::vector<Record> recordArray;
    // initiate record object/struct (?)
    Record current; // will be reused
    // Get each full line
    std::string line;
    while (getline(file, line)) {
        // an empty line indicates a new record is being recorded
        if (line.empty()) {
            recordArray.push_back(current);
            std::cout << current.cid << std::endl;
            // remove contents of last record
            current.clearRecord();
        }
        // putting the line in a istringstream to feed word by word to attr
        std::istringstream iss(line);
        std::string attr;
        while (iss >> attr) {
            // split into key value pair
            std::string key = attr.substr(0,3);
            std::string value = attr.substr(4, attr.npos);
            // TODO probably a less disgusting way to do this...
            if      (key == "byr") { current.byr = value; }
            else if (key == "iyr") { current.iyr = value; }
            else if (key == "eyr") { current.eyr = value; }
            else if (key == "hgt") { current.hgt = value; }
            else if (key == "hcl") { current.hcl = value; }
            else if (key == "ecl") { current.ecl = value; }
            else if (key == "pid") { current.pid = value; }
            else if (key == "cid") { current.cid = value; }
        }
    }
    // account for last record
    recordArray.push_back(current);
    std::cout << current.cid << std::endl;
    return recordArray;
}

bool validateRecord(Record record) {
    // 1. All 8 fields are present: Valid
    // 2. cid is not present but all others are: Valid
    // 3. cid is not present and 1-6 other fields are present: Invalid
    // 4. cid is present, but another field is not: Invalid
    if      (record.byr == "") {return false; }
    else if (record.iyr == "") {return false; }
    else if (record.eyr == "") {return false; }
    else if (record.hgt == "") {return false; }
    else if (record.hcl == "") {return false; }
    else if (record.ecl == "") {return false; }
    else if (record.pid == "") {return false; }
    else { // All 8 fields are present -- ignore cid
        return true;
    }
}

int main(int argc, char* argv[]) {
    // verify arguments
    if (argc < 2) {
        printf("Please specify input file\n");
        return -1;
    }
    std::string filename = argv[1];
    // get record array
    std::vector<Record> records;
    records = readRecordFile(filename);

    uint32_t validRecords = 0;
    for (int i=0; i < records.size(); ++i) {
        if (validateRecord(records[i])) {
            validRecords++;
            printf("Record %d is valid.\n", i+1);
        }
    }
    std::cout << "Number of valid records: " << validRecords << std::endl;
    return 0;
}
