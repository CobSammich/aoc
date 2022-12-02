"""
Implementation for AOC 2021 Day 2 Problem 1
"""

from typing import Any, Callable
import sys
import numpy as np
import ipdb


def read_input(filename: str) -> np.ndarray:
    """
    Returns a 2D array of the bits
    """
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    bit_array = []
    for line in lines:
        bit_array.append([int(bit) for bit in line])

    bit_array = np.array(bit_array)
    return bit_array

def solve(data: np.ndarray) -> int:
    """

    """
    oxygen = rating(data, bias=1)[0]
    co2 = rating(data, bias=0)[0]
    ipdb.set_trace()
    print(f"oxygen: {oxygen}")
    print(f"co2: {co2}")

    bit_vals = [2**n for n in range(len(co2))][::-1]

    # binary to decimal
    oxygen_decimal = np.sum(bit_vals * oxygen)
    co2_decimal = np.sum(bit_vals * co2)
    return oxygen_decimal * co2_decimal

def rating(data: np.ndarray, depth:int = 0, bias:int = 1) -> Any[np.ndarray, Callable]:
    """
    Recursively run through each vertical sequence of bits. Do logic until one binary array is left
    bias: 1 for oxygen, 0 for CO2
    """
    if len(data) == 1:
        return data
    n_ones = np.sum(data[:, depth] == 1)
    n_zeros = np.sum(data[:, depth] == 0)

    ones = data[data[:, depth] == 1]
    zeros = data[data[:, depth] == 0]
    # General -- not space efficient
    biased = data[data[:, depth] == bias]
    depth += 1

    # AHHHH LOGIC
    if n_ones == n_zeros:
        return rating(biased, depth, bias)
    elif np.logical_xor(n_ones > n_zeros, not bias):
        return rating(ones, depth, bias)
    elif np.logical_xor(n_ones < n_zeros, not bias):
        return rating(zeros, depth, bias)

def main():
    data = read_input(sys.argv[1])
    answer = solve(data)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()

