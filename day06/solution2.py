"""
Implementation for AOC 2021 Day 6 Problem 2
"""

from typing import List, Tuple
import sys
import numpy as np
import ipdb


def read_input(filename: str) -> List[int]:
    """
    Returns a 1D array of the lanternfish ages
    """
    with open(filename) as f:
        lines = f.readlines()[0]  # should be only one line

    days = [int(s) for s in lines.strip().split(',')]
    return days


def initialize_lanternfish_list(days_list: List[int]) -> np.ndarray:
    """
    The list here is different than day 1. It stores an array of length 9 for the number of days
    left that are possible for a lanternfish to reproduce. Each number at an index represents the
    number of fish that have that many days left until they reproduce.
    """
    days_left = np.zeros((9), dtype=np.int64)
    for days in days_list:
        days_left[days] += 1
    return days_left


def simulate_n_days(n_days: int, days_left: List[int]) -> List[int]:
    """
    simulate n_days and return

    """
    for day in range(n_days):
        # Get the number that will reproduce today
        n_fish_rollover = days_left[0]
        days_left = np.roll(days_left, -1)
        # Add the fish that just reproduced to the 6th day
        days_left[6] += n_fish_rollover
    return days_left


def main():
    days = read_input(sys.argv[1])
    n_days_to_simulate = int(sys.argv[2])
    days_left = initialize_lanternfish_list(days)
    # ipdb.set_trace()
    days_left = simulate_n_days(n_days_to_simulate, days_left)
    print(f"After {n_days_to_simulate} days, there are {np.sum(days_left)} fish.")
    # ipdb.set_trace()
    answer = np.sum(days_left)
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    main()
