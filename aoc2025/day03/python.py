import argparse
import bisect


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data):
    max_values = []
    for line in data:
        max_value_line = 0
        for i, value in enumerate(line):
            for j, value2 in enumerate(line[i + 1 :]):
                curr_val = int(value + value2)
                if curr_val > max_value_line:
                    max_value_line = curr_val
        max_values.append(max_value_line)
    return sum(max_values)


def part2(data):
    NUM_ALLOWED = 12
    max_values = []
    for line in data:
        line_values = [int(v) for v in line]
        # base case
        indices_to_keep = [-1]
        values_to_keep = []
        for index in range(NUM_ALLOWED):
            max_value = max(
                line_values[
                    indices_to_keep[-1] + index + 1 : len(line_values)
                    - NUM_ALLOWED
                    + index
                    + 1
                ]
            )
            max_index = indices_to_keep[-1] + line_values[
                indices_to_keep[-1] + index + 1 : len(line_values)
                - NUM_ALLOWED
                + index
                + 1
            ].index(max_value)
            indices_to_keep.append(max_index)
            values_to_keep.append(max_value)
        best_values = [str(v) for v in values_to_keep]
        max_values.append(int("".join(best_values)))
    return sum(max_values)


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
