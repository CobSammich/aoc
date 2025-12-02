import argparse


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data):
    dial = 50
    num_point_at_zero = 0
    for line in data:
        direction = line[0]
        magnitude = int(line[1:])
        if direction == "L":
            magnitude *= -1

        dial += magnitude
        dial %= 100
        if dial == 0:
            num_point_at_zero += 1

    return num_point_at_zero


def part2(data):
    dial = 50
    num_pass_zero = 0
    for line in data:
        direction = line[0]
        magnitude = int(line[1:])

        curr_rotation_pass_zero, magnitude = divmod(magnitude, 100)

        if direction == "L":
            magnitude *= -1
        new_dial = (dial + magnitude) % 100

        if new_dial == 0:
            num_pass_zero += 1
        elif direction == "L" and dial != 0 and new_dial > dial:
            num_pass_zero += 1
        elif direction == "R" and dial != 0 and new_dial < dial:
            num_pass_zero += 1

        num_pass_zero += curr_rotation_pass_zero

        dial = new_dial

    return num_pass_zero


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
