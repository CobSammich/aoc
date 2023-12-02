import argparse
import ipdb
from dataclasses import dataclass
import numpy as np
import sys


@dataclass
class Game:
    red: int = 0
    green: int = 0
    blue: int = 0


def make_game(game_str: str) -> Game:
    colors = game_str.split(',')

    game = Game()
    for color in colors:
        num, c = color.split()
        print(num, c)
        num = int(num)
        match c:
            case "red":
                game.red = num
            case "green":
                game.green = num
            case "blue":
                game.blue = num
    return game


def read_input(filename: str) -> dict[str, list[Game]]:
    data: dict[str, list[Game]] = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            game_id = line.split(':')[0].split()[-1]
            data[game_id] = []

            games = line.split(':')[-1].split(';')
            for game_str in games:
                game_str.split()
                game = make_game(game_str)
                data[game_id].append(game)
    return data


def validate_game(game: Game) -> bool:
    if game.red > 12:
        return False
    if game.green > 13:
        return False
    if game.blue > 14:
        return False
    return True


def part1(data: dict[str, list[Game]]):
    val = 0
    for id, games in data.items():
        valid_games = np.array([validate_game(game) for game in games])
        if not valid_games.all():
            continue
        # otherwise add the id's
        val += int(id)
    return val


def find_power_set(games: list[Game]) -> float:
    p_game = Game(
        red=sys.maxsize,
        green=sys.maxsize,
        blue=sys.maxsize,
    )
    p_game = Game(
        red=0,
        green=0,
        blue=0,
    )
    for game in games:
        print(game)
        if game.red > p_game.red:
            p_game.red = game.red
        if game.green > p_game.green:
            p_game.green = game.green
        if game.blue > p_game.blue:
            p_game.blue = game.blue

    return p_game.red * p_game.blue * p_game.green


def part2(data):
    val = 0
    for id, games in data.items():
        p = find_power_set(games)
        val += p
    return val


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
