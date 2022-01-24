"""
Implementation for AOC 2021 Day 4 Problem 2
"""

from typing import List, Tuple
import sys
import numpy as np
import ipdb

BOARD_WIDTH = 5
BOARD_HEIGHT = 5


def read_input(filename: str) -> Tuple[List[int], np.ndarray]:
    """
    Returns a 2D array of the bits
    """
    with open(filename) as f:
        lines = f.readlines()

    draw_order = [int(v) for v in lines[0].strip().split(',')]
    # number of board = len(lines[2:]) // 6
    n_boards = len(lines[1:]) // 6
    # init boards
    boards = np.zeros((n_boards, BOARD_WIDTH, BOARD_HEIGHT), dtype=int)
    for i in range(n_boards):
        # get rid of the newline row -- idk what's happening here
        board = lines[i*(BOARD_HEIGHT + 1) + 2: i*(BOARD_HEIGHT + 1) + (2 + BOARD_WIDTH)]
        new_board = np.zeros((BOARD_WIDTH, BOARD_HEIGHT), dtype=int)
        # iterate ove all rows and convert values to int
        for i_row, row in enumerate(board):
            new_row = [v for v in row.strip().split(' ') if v != '']
            # set the new row
            new_board[i_row, :] = new_row
        boards[i] = new_board
    return draw_order, boards


def check_for_winner(boards: np.ndarray, board_masks: np.ndarray) -> np.ndarray:
    """
    Returns whether each board has won or not
    """
    winning_boards = np.zeros((len(boards)), dtype=bool)
    for board_index, board in enumerate(board_masks):
        for row in board:
            if (row is True).all():
                winning_boards[board_index] = True
        for col in board.T:
            if (col is True).all():
                winning_boards[board_index] = True
    return winning_boards


def solve(draw_order, boards: np.ndarray) -> int:
    """
    """
    # Keep track of what numbers have been called
    board_masks = np.zeros_like(boards, dtype=bool)

    for draw_idx, drawn_number in enumerate(draw_order):
        for i_board, board in enumerate(boards):
            ixs = np.where(board == drawn_number)
            # ipdb.set_trace()
            if ixs is not None:
                board_masks[i_board][ixs[0], ixs[1]] = True

        # check if someone has won
        winning_boards = check_for_winner(boards, board_masks)
        # Get all the losing boards
        losing_board_indices = np.arange(len(winning_boards))[winning_boards is False]
        if len(losing_board_indices) == 1:
            # Get the final remaining board
            losing_board = boards[losing_board_indices]
            losing_board_mask = board_masks[losing_board_indices]
            # iterate through the rest of the numbers until this board wins
            # THIS IS DONE POORLY
            print(f"draw: {drawn_number}")
            for drawn_number in draw_order[draw_idx:]:
                ixs = np.where(losing_board[0] == drawn_number)
                print(f"draw: {drawn_number}")
                if ixs is not None:
                    losing_board_mask[0][ixs[0], ixs[1]] = True

                final_win = check_for_winner(losing_board, losing_board_mask)
                if final_win:
                    unmarked_numbers = losing_board[losing_board_mask is False]
                    return np.sum(unmarked_numbers) * drawn_number


def main():
    draw_order, boards = read_input(sys.argv[1])
    answer = solve(draw_order, boards)
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    main()
