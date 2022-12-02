"""
Implementation for AOC 2021 Day 2 Problem 1
"""

jflsdkjflsdkfj

import sys

import numpy as np


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
    doc

    """
    gamma = np.mean(data, axis=0) > 0.5
    # flip bits
    epsilon = np.array([False]*len(gamma)) == gamma

    bit_vals = [2**n for n in range(len(gamma))][::-1]

    # binary to decimal
    gamma_decimal = np.sum(bit_vals * gamma)
    epsilon_decimal = np.sum(bit_vals * epsilon)
    return gamma_decimal * epsilon_decimal


def main():
    """
    doc
    """
    data = read_input(sys.argv[1])
    answer = solve(data)
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    main()
