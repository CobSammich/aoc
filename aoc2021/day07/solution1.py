"""
Implementation for AOC 2021 Day 7 Problem 1
"""

from typing import List, Tuple
import sys
import numpy as np
import ipdb

def read_input(filename: str) -> List[int]:
    """
    Reads data from the given filename and returns the list of integers corresponding to the
    horizontal positions.

    Parameters
    ----------
    filename : str
        the filename to read as input

    Returns
    -------
    List[int]
        The horizontal positions of

    """
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()[0] #should be only one line

    crab_positions = [int(s) for s in lines.strip().split(',')]
    return crab_positions

def compute_fuel_cost(position: int, positions: List[int]) -> int:
    """
    Given a horizontal position, `position`, and a list of positions to search through, compute the
    fuel cost for that position. The fuel cost is equivalent to the difference between each position
    from the given position.

    Parameters
    ----------
    position : int
        position
    positions : List[int]
        positions

    Returns
    -------
    int
        The

    """
    fuel_costs = []
    for curr_position in positions:
        fuel_cost = np.abs(curr_position - position)
        fuel_costs.append(fuel_cost)
    return np.sum(fuel_costs)

def solve(positions: List[int]) -> int:
    fuel_costs = []
    for pos in positions:
        fuel_cost = compute_fuel_cost(pos, positions)
        fuel_costs.append(fuel_cost)
    # Find where the fuel cost was the least
    min_cost_index = np.where(fuel_costs == np.min(fuel_costs))[0]
    print(min_cost_index)
    return fuel_costs[min_cost_index[0]]

def main():
    """
    Main driver for solution
    """
    positions = read_input(sys.argv[1])
    print(positions)
    answer = solve(positions)
    #print(f"Horizontal position of least fuel consumption: {answer}")
    print(f"Best Fuel consumption: {answer}")
    #answer = np.sum(days_left)
    #print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()

