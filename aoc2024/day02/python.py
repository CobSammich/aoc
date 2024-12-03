import argparse
import ipdb
import numpy as np


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def level_is_safe(levels: list[int]) -> bool:
    if levels[1] > levels[0]:
        increasing = True
    elif levels[1] < levels[0]:
        increasing = False
    else:
        return False

    for i, level in enumerate(levels[:-1]):
        diff = levels[i + 1] - level
        if not increasing:
            diff *= -1
        if diff > 3 or diff < 1:
            return False
    return True


def part1(data):
    n_safe = 0
    for line in data:
        levels = [int(v) for v in line.split()]
        if level_is_safe(levels):
            n_safe += 1
    return n_safe


def part2(data):
    n_safe = 0
    for line in data:
        levels = [int(v) for v in line.split()]
        if level_is_safe(levels):
            n_safe += 1
        else:
            safe_levels = 0
            # Check if there's 1 safe combination
            for i in range(len(levels)):
                levels_copy = levels.copy()
                levels_copy.pop(i)
                if level_is_safe(levels_copy):
                    safe_levels += 1
            if safe_levels > 0:
                n_safe += 1
    return n_safe


def main(filename: str):
    data = read_input(filename)
    p1_answer = part1(data)
    print(f"Part 1 Answer: {p1_answer}")
    p2_answer = part2(data)
    print(f"Part 2 Answer: {p2_answer}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code")
    # Add the command line argument for the filename
    parser.add_argument("filename", type=str, help="Path to the dataset file")
    # Parse the command line arguments
    args = parser.parse_args()

    main(args.filename)
