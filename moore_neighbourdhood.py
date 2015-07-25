#!/usr/bin/env
# -*- coding:utf-8 -*-
# moore_neighbourdhood.py

def count_neighbours(grid, row, col):
    m = grid
    max_row = len(m) - 1
    max_col = len(m[0]) - 1
    conditions = all((all((row <= max_row , row >= 0)), all((col <= max_col, col >= 0))))

    if not conditions:
        return 'Error'

    r_lower = row - 1 if row > 1 else 0
    r_upper = row + 1 if row < max_row else max_row
    c_lower = col - 1 if col > 1 else 0
    c_upper = col + 1 if col < max_col else max_col
    count = 0

    for irow in range(r_lower, r_upper + 1):
        for icol in range(c_lower, c_upper + 1):
            count += m[irow][icol]

    return count - m[row][col]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
