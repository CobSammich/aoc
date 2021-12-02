"""
Implementation for AOC 2021 Day 2 Problem 1
"""

from typing import List
import sys
import pdb

def read_input(filename: str) -> List[int]:
    """
    Reads the sonar measurements file and formats it into ints.
    """
    with open(filename) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        vals = line.strip().split(" ")
        vals[1] = int(vals[1])
        data.append(vals)
    return data

def solve(data) -> int:
    """

    """
    xpos = 0
    ypos = 0
    for move in data:
        if move[0] == "forward":
            xpos += move[1]
        elif move[0] == "down":
            ypos += move[1]
        elif move[0] == "up":
            ypos -= move[1]
        else:
            print(f"Invalid Movement: {move[0]}")
    return xpos*ypos

def main():
    data = read_input(sys.argv[1])
    answer = solve(data)
    print(f"The answer is: {answer}.")

if __name__ == "__main__":
    main()

