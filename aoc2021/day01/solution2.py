"""
Implementation for AOC 2021 Day 1 Problem 2
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


def solve(sonar_measurements: List, k=3) -> int:
    """
    Run a sliding window of size k over the collected data, sum values in the window and count the
    number of times the sum increases
    """
    n_increased = 0
    last_index = -k + 1
    for i, _ in enumerate(sonar_measurements[:last_index]):
        # sliding window of k=3
        val = sum(sonar_measurements[i:i + k])
        # initial sample -- can't increase or decrease
        if i == 0:
            last_val = val
            print(f"{val} (N/A - no previous sum")
            continue
        if val > last_val:
            n_increased += 1
            print(f"{val} ({Color.BOLD}{Color.GREEN}increased{Color.END})")
        else:
            print(f"{val} ({Color.RED}decreased){Color.END}")
        last_val = val
    return n_increased


def main():
    sonar_measurements = read_input(sys.argv[1])
    answer = solve(sonar_measurements, k=3)
    print(f"The answer is: {answer}.")


if __name__ == "__main__":
    main()
