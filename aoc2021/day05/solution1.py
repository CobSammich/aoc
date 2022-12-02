"""
Implementation for AOC 2021 Day 5 Problem 1
"""

from typing import List, Tuple
import sys
import numpy as np
import ipdb


class Vent:
    """
    Defines two 2D points that the vent covers

    Could also take inputs of points where a point is P(x, y)
    """

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        """ Defines print information for Vent points """
        s = f"Vent: ({self.x1},{self.y1}), ({self.x2},{self.y2})"
        return s

    def point_coverage(self):
        """
        Computes the line between the two points, and returns them as a list of points
        """
        diff_x = self.x2 - self.x1
        diff_y = self.y2 - self.y1
        # movement of x and y per step:
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        # inclusive of last element, so +1
        n_points = max(abs(dx), abs(dy)) + 1
        # For now only consider horizontal or vertical lines
        if abs(dx) == abs(dy):
            return None
        # normalize dx,dy
        if dx != 0:
            dx = dx // abs(dx)
        if dy != 0:
            dy = dy // abs(dy)
        # vector of points in the form: (x, y)
        points = []
        curr_x, curr_y = self.x1, self.y1
        for i in range(n_points):
            p = curr_x, curr_y
            points.append(p)
            # Increment to next point
            curr_x += dx
            curr_y += dy
        return points


def read_input(filename: str) -> List[Vent]:
    """
    Returns a 2D array of the bits
    """
    with open(filename) as f:
        lines = f.readlines()

    vents = []  # array of Vent objects
    # split " -> " into two tuples of points
    points = [line.strip().split(' -> ') for line in lines]
    for point_pair in points:
        p1, p2 = point_pair
        x1, y1 = [int(p) for p in p1.split(',')]
        x2, y2 = [int(p) for p in p2.split(',')]
        curr_vent = Vent(x1, y1, x2, y2)
        vents.append(curr_vent)
    return vents


def initialize_vent_field(vents: List[Vent]) -> np.ndarray:
    """
    Gets the size needed to store the vent field from the max x and y values. Returns a 2D array
    initialized with zeros of the size of the vent field.
    """
    # O(n) pass through all vents to get the largest x and y values. Lowest can be assumed to be 0
    # and 1
    max_x, max_y = 0, 0
    for vent in vents:
        # X
        if vent.x1 > max_x:
            max_x = vent.x1
        if vent.x2 > max_x:
            max_x = vent.x2
        # Y
        if vent.y1 > max_y:
            max_y = vent.y1
        if vent.y2 > max_y:
            max_y = vent.y2
    vent_field = np.zeros((max_y+1, max_x+1), dtype=int)
    return vent_field


def solve(vents: List[Vent]) -> np.ndarray:
    # form vent field
    vent_field = initialize_vent_field(vents)
    # compute the line each vent covers
    for vent in vents:
        # list of points
        points = vent.point_coverage()
        # in case of diagonal line
        if points is None:
            continue
        # iterate over all points and increment their positions in the vent field.
        for point in points:
            x, y = point
            vent_field[y, x] += 1
    # Find the number of points where at least two lines overlap:
    answer = len(np.where(vent_field >= 2)[0])
    return answer


def main():
    vents = read_input(sys.argv[1])
    answer = solve(vents)
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    main()
