"""
Implementation for AOC 2021 Day 1 Problem 1
"""

from typing import List
import sys

from colors import Color


def read_input(filename: str) -> List[int]:
    """
    Reads the sonar measurements file and formats it into ints.
    """
    with open(filename) as f:
        lines = f.readlines()
    sonar_measurements = [int(line.strip()) for line in lines]
    return sonar_measurements


def solve(sonar_measurements: List) -> int:
    """
    Iterates over all sonar measurements and counts how many were larger than the last.
    """
    n_increased = 0
    # iterate until the last one
    for i, sonar in enumerate(sonar_measurements[:-1]):
        if i == 0:
            print(f"{sonar} (N/A - no previous measurement")
        # This one is larger than the previous one
        if sonar_measurements[i+1] > sonar:
            n_increased += 1
            print(f"{sonar} ({Color.BOLD}{Color.GREEN}increased{Color.END})")
        else:
            print(f"{sonar} ({Color.RED}decreased){Color.END}")
    return n_increased


def main():
    sonar_measurements = read_input(sys.argv[1])
    answer = solve(sonar_measurements)
    print(f"The answer is: {answer}.")


if __name__ == "__main__":
    main()
