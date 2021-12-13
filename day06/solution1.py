"""
Implementation for AOC 2021 Day 6 Problem 1
"""

from typing import List, Tuple
import sys
import numpy as np
import ipdb

class LanternFish:
    """
    A lanternfish object. The 'days' variable determines how many days until it reproduces.
    """
    def __init__(self, days: int):
        """
        days is the number of days until it reproduces
        """
        self.days = days

    def __str__(self) -> str:
        """ Defines print information for Vent points """
        s = f"LanternFish: {self.days} until it reproduces."
        return s

    def age(self) -> bool:
        """
        Makes the days to reproduce of the lanternfish decrease by one and returns whether it should
        produce a new lanternfish or not.
        """
        self.days -= 1
        if self.days == -1:
            self.days = 6
            return True
        return False

def read_input(filename: str) -> List[int]:
    """
    Returns a 1D array of the lanternfish ages
    """
    with open(filename) as f:
        lines = f.readlines()[0] #should be only one line

    days = [int(s) for s in lines.strip().split(',')]
    return days

def initialize_lanternfish_list(days_list: List[int]) -> np.ndarray:
    """
    """
    fishes = []
    for i, days in enumerate(days_list):
        temp_fish = LanternFish(days)
        fishes.append(temp_fish)
    return fishes

def simulate_n_days(n_days: int, fishes: List[LanternFish]) -> np.ndarray:
    for day in range(n_days):
        current_fishes_today = len(fishes)
        for i_fish in range(current_fishes_today):
            fish = fishes[i_fish]
            # age returns true if it has reproduced, so we must make a new lanternfish
            if fish.age():
                new_fish = LanternFish(8)
                fishes.append(new_fish)
    return fishes

def main():
    days = read_input(sys.argv[1])
    n_days_to_simulate = int(sys.argv[2])
    fishes = initialize_lanternfish_list(days)
    for fish in fishes:
        print(fish)
    #ipdb.set_trace()
    simulate_n_days(n_days_to_simulate, fishes)
    print(f"After {n_days_to_simulate} days, there are {len(fishes)} fish.")
    for fish in fishes:
        print(fish)
    #ipdb.set_trace()
    answer = len(fishes)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()

