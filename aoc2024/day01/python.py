import argparse
import ipdb
import numpy as np


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data):
    left = []
    right = []
    for line in data:
        values = line.split()
        left.append(int(values[0]))
        right.append(int(values[1]))

    left = np.array(sorted(left))
    right = np.array(sorted(right))

    summed_diff = sum(np.abs(left - right))
    return summed_diff


def part2(data):
    left = []
    right = []
    for line in data:
        values = line.split()
        left.append(int(values[0]))
        right.append(int(values[1]))

    keys, values = np.unique(right, return_counts=True)
    value_counts = {k: v for k, v in zip(keys, values)}

    similarity_score = 0
    for value in left:
        if value not in value_counts.keys():
            continue
        n_occurences = value_counts[value]
        similarity_score += value * n_occurences

    return similarity_score

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
