"""

Implementation for AOC 2021 Day 2 Problem 1
"""

import sys
from typing import List


def read_input(filename: str) -> List[int]:
    """
    Reads the movement log and outputs as a list of [str, int] with the format:
    [movement direction, units]
    """
    with open(filename, encoding="utf-8", mode='r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        vals = line.strip().split(" ")
        vals[1] = int(vals[1])
        data.append(vals)
    return data


def solve(data) -> int:
    """
    Given data in the form [[str, int], ...] calculate the distance moved in both the horizontal
    plane and the vertical plane. Vertical plane being depth. Multiplying your x and y displacements
    gives you the answer.

    In this case, however, the 'down' and 'up' movements actually change the "aim" (direction) the
    submarine is looking. These don't have any units, but when you make a "forward" move you make a
    depth movement of (aim * movement units).
    """
    xpos = 0
    ypos = 0
    aim = 0
    for move in data:
        if move[0] == "forward":
            xpos += move[1]
            ypos += move[1]*aim
        elif move[0] == "down":
            aim += move[1]
        elif move[0] == "up":
            aim -= move[1]
        else:
            print(f"Invalid Movement: {move[0]}")
    return xpos*ypos


def main():
    data = read_input(sys.argv[1])
    answer = solve(data)
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    main()
