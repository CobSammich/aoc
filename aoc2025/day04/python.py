import argparse

import numpy as np
from scipy.signal import convolve2d

KERNEL = np.array(
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
)


def read_input(filename: str) -> np.ndarray:
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    # okay to assume that each row's width is equal
    np_data = np.zeros((len(data), len(data[0])), dtype=bool)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "@":
                np_data[i, j] = 1

    return np_data


def part1(data):
    convolved = convolve2d(data, KERNEL)
    return sum(data[convolved[1:-1, 1:-1] < 4])


def part2(data):
    total_sum = 0
    while True:
        convolved = convolve2d(data, KERNEL)
        curr_sum = sum(data[convolved[1:-1, 1:-1] < 4])
        if curr_sum == 0:
            break
        total_sum += curr_sum
        data[convolved[1:-1, 1:-1] < 4] = False
    return total_sum


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
