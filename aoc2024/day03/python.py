import argparse
import ipdb
import numpy as np
import re


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def find_muls(line: str) -> list[tuple[int, int]]:
    regex = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(regex, line)
    matches = [(int(x[0]), int(x[1])) for x in matches]
    return matches


def find_all_instructions(line: str) -> list[str]:
    regex = r"mul\((-?\d+),(-?\d+)\)|do(.*?)\(\)"
    matches = re.findall(regex, line)
    return matches


def part1(data):
    sum = 0
    for line in data:
        matches = find_muls(line)
        for match in matches:
            sum += match[0] * match[1]
    return sum


def part2(data):
    sum = 0
    do = True
    for line in data:
        matches = find_all_instructions(line)
        for match in matches:
            if match[0] == "" and match[1] == "":
                if match[2] == "":
                    do = True
                else:
                    do = False
            elif do:
                sum += int(match[0]) * int(match[1])
    return sum


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
