import argparse
from dataclasses import dataclass
from enum import Enum


class Operation(Enum):
    MULTIPLY = "*"
    ADD = "+"


@dataclass
class Problem:
    numbers: list[int]
    operation: Operation

    def solve(self) -> int:
        if self.operation == Operation.ADD:
            return sum(self.numbers)
        elif self.operation == Operation.MULTIPLY:
            answer = 1
            for val in self.numbers:
                answer *= val
            return answer
        else:
            raise ValueError("")


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip().split() for line in f.readlines()]
    return data


def empty_column(num: list[str]) -> bool:
    for char in num:
        if char != " ":
            return False
    return True


def read_input2(filename: str):
    with open(filename, "r") as f:
        data = [line.strip("\n") for line in f.readlines()]
    max_width = max([len(line) for line in data])
    # pad with empty to avoid index errors
    for i, line in enumerate(data):
        data[i] += " " * (max_width - len(line))

    return data


def part1(data):
    num_problems = len(data[0])
    answer = 0
    for i in range(num_problems):
        curr_vals = [int(arr[i]) for arr in data[:-1]]
        problem = Problem(curr_vals, Operation(data[-1][i]))
        answer += problem.solve()
    return answer


def part2(data):
    num_rows = len(data)
    num_cols = len(data[0])

    nums = []
    all_nums = []

    for col in range(num_cols):
        num = [data[row][col] for row in range(num_rows - 1)]

        if empty_column(num):
            all_nums.append(nums)
            nums = []
        else:
            num = int("".join(num))
            nums.append(num)

    all_nums.append(nums)
    operations = data[-1].split()

    assert len(operations) == len(all_nums), "something is wrong..."

    answer = 0
    for numbers, operation in zip(all_nums, operations):
        problem = Problem(numbers, Operation(operation))
        answer += problem.solve()
    return answer


def main(filename: str):
    data = read_input(filename)
    p1_answer = part1(data)
    print(f"Part 1 Answer: {p1_answer}")
    data2 = read_input2(filename)
    p2_answer = part2(data2)
    print(f"Part 2 Answer: {p2_answer}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code")
    # Add the command line argument for the filename
    parser.add_argument("filename", type=str, help="Path to the dataset file")
    # Parse the command line arguments
    args = parser.parse_args()

    main(args.filename)
