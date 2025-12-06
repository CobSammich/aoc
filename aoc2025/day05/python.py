import argparse


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def create_fresh_map(data) -> dict:
    fresh_map = {}
    for line in data:
        if len(line) == 0:
            break
        lower, upper = line.split("-")
        lower, upper = int(lower), int(upper)
        for i in range(lower, upper + 1):
            fresh_map[i] = True

    return fresh_map


def split_data(data) -> tuple[list[str], list[str]]:
    for line_id, line in enumerate(data):
        if len(line) == 0:
            return data[:line_id], data[line_id + 1 :]
    raise LookupError("Could not find empty line in data indicating split")


def part1(data):
    id_range_data, id_data = split_data(data)
    num_fresh = 0
    for ingredient_id in id_data:
        ingredient_id = int(ingredient_id)
        for id_range in id_range_data:
            lower, upper = id_range.split("-")
            lower, upper = int(lower), int(upper)
            if ingredient_id >= lower and ingredient_id <= upper:
                num_fresh += 1
                break

    return num_fresh


def part2(data):
    fresh_map = create_fresh_map(data)
    return sum(fresh_map.values())
    # id_range_data, _ = split_data(data)
    # num_fresh = 0
    # for id_range in id_range_data:
    #     lower, upper = id_range.split("-")
    #     lower, upper = int(lower), int(upper)
    #     num_fresh += upper - lower
    # return num_fresh


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
