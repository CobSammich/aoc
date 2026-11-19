#include <fstream>
#include <iostream>
#include <vector>

struct Rotation {
  char direction;
  int magnitude;
};

std::vector<Rotation> readInputFile(const std::string& filename) {
  std::vector<Rotation> rotations;

  std::ifstream infile(filename);

  std::string line;
  while (std::getline(infile, line)) {
    char direction = line[0];
    int magnitude = std::stoi(line.substr(1, line.size()));
    Rotation rotation = {direction, magnitude};
    rotations.push_back(rotation);
  }
  return rotations;
}

int part1(std::vector<Rotation> input) {
  int dial = 50;
  int numPointAtZero = 0;
  for (Rotation rotation : input) {

    if (rotation.direction == 'L') {
      rotation.magnitude *= -1;
    }

    dial += rotation.magnitude;
    dial %= 100;
    if (dial == 0) {

      numPointAtZero++;
    }
  }

  return numPointAtZero;
}

int part2(std::vector<Rotation> input) {
  int dial = 50;
  int numPassZero = 0;
  for (Rotation rotation : input) {

    int currRotationPassZero = rotation.magnitude / 100;
    int newMagnitude = rotation.magnitude % 100;

    if (rotation.direction == 'L') {
      newMagnitude *= -1;
    }
    int newDial = (dial + newMagnitude) % 100;
    if (newDial < 0) {
      // -18 % 100 in rust doesn't = 82, so do this
      newDial += 100;
    }

    if (newDial == 0) {
      numPassZero += 1;
    }
    else if (rotation.direction == 'L' && dial != 0 && newDial > dial) {
      numPassZero += 1;
    }
    else if (rotation.direction == 'R' && dial != 0 && newDial < dial) {
      numPassZero += 1;
    }

    numPassZero += currRotationPassZero;

    dial = newDial;
  }
  return numPassZero;
}

int main(int argc, char* argv[]) {
  std::vector<Rotation> rotations = readInputFile(argv[1]);

  int p1_answer = part1(rotations);
  std::cout << "Part 1: " << p1_answer << std::endl;

  int p2_answer = part2(rotations);
  std::cout << "Part 2: " << p2_answer << std::endl;

  return 0;
}
