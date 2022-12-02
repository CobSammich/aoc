import heapq
import sys
from typing import List

import numpy as np


def read_input(filename: str) -> List[List[int]]:
    with open(filename, mode="r") as f:
        all_elves: List[List[int]] = []
        curr_buffer: List[int] = []
        for line in f.readlines():
            line = line.strip()
            if line == '':
                all_elves.append(curr_buffer)
                curr_buffer = []
            else:
                curr_buffer.append(int(line))
    # get the final buffer too
    all_elves.append(curr_buffer)
    return all_elves


def part1(data: List[List[int]]) -> int:
    total_cals = [sum(elf) for elf in data]
    answer = max(total_cals)
    return answer


def part2(data: List[List[int]]) -> int:
    total_cals = [sum(elf) for elf in data]
    largest3 = heapq.nlargest(3, total_cals)
    return np.sum(largest3)


def main():
    input_file = sys.argv[1]
    data = read_input(input_file)
    p1_answer = part1(data)
    print(f"Part1 Answer: {p1_answer}")
    p2_answer = part2(data)
    print(f"Part2 Answer: {p2_answer}")


if __name__ == "__main__":
    main()
