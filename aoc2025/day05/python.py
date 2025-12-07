import argparse


def read_input(filename: str):
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data


def split_data(data) -> tuple[list[str], list[str]]:
    for line_id, line in enumerate(data):
        if len(line) == 0:
            return data[:line_id], data[line_id + 1 :]
    raise LookupError("Could not find empty line in data indicating split")


def get_bounds(id_range: str) -> tuple[int, int]:
    lower, upper = id_range.split("-")
    return int(lower), int(upper)


def part1(data):
    id_range_data, id_data = split_data(data)
    num_fresh = 0
    for ingredient_id in id_data:
        ingredient_id = int(ingredient_id)
        for id_range in id_range_data:
            lower, upper = get_bounds(id_range)
            if ingredient_id >= lower and ingredient_id <= upper:
                num_fresh += 1
                break

    return num_fresh


def in_between(val, lower, upper):
    return val >= lower and val <= upper


def split_bounds(id_range_data):
    lowers, uppers = [], []
    for id_range in id_range_data:
        lower, upper = get_bounds(id_range)
        lowers.append(lower)
        uppers.append(upper)
    return sorted(lowers), sorted(uppers)


def part2(data):
    id_range_data, _ = split_data(data)
    num_fresh = 0

    lowers, uppers = split_bounds(id_range_data)
    combined = sorted(lowers + uppers)
    counter = 0
    # keep track of the first lower bound
    curr_lower = lowers[0]
    reconstructed_bounds = []
    for bound in combined:
        if len(lowers) != 0 and bound == lowers[0]:
            counter += 1
            lowers.remove(bound)
        elif len(lowers) != 0 and bound == uppers[0]:
            counter -= 1
            uppers.remove(bound)

        if counter == 0:
            reconstructed_bounds.append((curr_lower, bound))
            curr_lower = lowers[0]
        if bound == combined[-1]:
            reconstructed_bounds.append((curr_lower, bound))

    num_fresh = 0
    for bounds in reconstructed_bounds:
        lower, upper = bounds
        num_fresh += upper - lower + 1
    return num_fresh


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
