import argparse

import numpy as np


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data: list[str]):
    start_index = data[0].find("S")
    beam_indices = set([start_index])
    num_splits = 0
    for row in range(len(data)):
        new_beam_indices = beam_indices.copy()
        for beam_index in beam_indices:
            if data[row][beam_index] == "^":
                num_splits += 1
                new_beam_indices.remove(beam_index)
                new_beam_indices.add(beam_index - 1)
                new_beam_indices.add(beam_index + 1)
        beam_indices = new_beam_indices

    return num_splits


def quantum_beam(data: list[str], beam_index: int, row: int, table: np.ndarray):
    # base case:
    if row == len(data):
        return 1
    if table[row][beam_index] != 0:
        return table[row][beam_index]
    if data[row][beam_index] == "^":
        table[row][beam_index] = quantum_beam(
            data,
            beam_index - 1,
            row + 1,
            table,
        ) + quantum_beam(
            data,
            beam_index + 1,
            row + 1,
            table,
        )
    else:
        table[row][beam_index] = quantum_beam(data, beam_index, row + 1, table)
    return table[row][beam_index]


def part2(data):
    beam_index = data[0].find("S")
    rows, cols = len(data), len(data[0])
    table = np.zeros((rows, cols), dtype=np.int64)
    paths = quantum_beam(data, beam_index, 0, table)
    return paths


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
