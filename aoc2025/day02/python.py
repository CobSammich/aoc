import argparse


def read_input(filename: str):
    with open(filename, "r") as f:
        data = f.read().strip().split(",")
    return data


def part1(data):
    id_sum = 0
    for id_range in data:
        lower, upper = id_range.split("-")
        for id in range(int(lower), int(upper) + 1):
            str_id = str(id)
            # if the number does not have an even number of digits, then it cannot be invalid
            if len(str_id) % 2 == 1:
                continue
            first_half = str_id[: len(str_id) // 2]
            second_half = str_id[len(str_id) // 2 :]
            if first_half == second_half:
                id_sum += int(str_id)
    return id_sum


def part2(data):
    id_sum = 0
    for id_range in data:
        lower, upper = id_range.split("-")
        for id in range(int(lower), int(upper) + 1):
            str_id = str(id)

            for substr_len in range(1, len(str_id) // 2 + 1):
                # print(f"{substr_len}, {str_id}")
                if len(str_id) % substr_len != 0:
                    # cannot break up this string into equal length parts
                    continue

                substrings = [
                    str_id[i : i + substr_len]
                    for i in range(0, len(str_id), substr_len)
                ]

                if len(set(substrings)) == 1:
                    id_sum += int(str_id)
                    # Make sure not to count this id more than once
                    break

    return id_sum


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
