import ipdb
import argparse
import re
import sys


def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data: list[str]) -> float:
    sum = 0
    for line in data:
        # Find all integers in the string
        ints = [s for s in line if s.isdigit()]
        if len(ints) != 0:
            sum += int(ints[0] + ints[-1])
    return sum


def part2(data: list[str]) -> float:
    digit_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    sum = 0
    for line in data:
        smallest_index = sys.maxsize
        smallest_int = 0
        largest_index = -1
        largest_int = 0
        for digit_str, digit_int in digit_map.items():
            # find all instances of the digit string in the string
            indices = [match.start() for match in re.finditer(digit_str, line)]
            # keep track of the smallest digit
            min_indices = indices.copy()
            max_indices = indices.copy()
            min_indices.append(smallest_index)
            max_indices.append(largest_index)
            if min(min_indices) < smallest_index:
                smallest_index = min(min_indices)
                smallest_int = digit_int
            if max(max_indices) > largest_index:
                largest_index = max(max_indices)
                largest_int = digit_int
        sum += int(str(smallest_int) + str(largest_int))
    return sum


def main(filename: str):
    data = read_input(filename)
    p1_answer = part1(data)
    print(f"Part 1 Answer: {p1_answer}")
    p2_answer = part2(data)
    print(f"Part 2 Answer: {p2_answer}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advent of Code')
    # Add the command line argument for the filename
    parser.add_argument('filename', type=str, help='Path to the dataset file')
    # Parse the command line arguments
    args = parser.parse_args()

    main(args.filename)
