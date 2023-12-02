import argparse
import ipdb

def read_input(filename: str):
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data

def part1(data):
    raise NotImplementedError()

def part2(data):
    raise NotImplementedError()

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
