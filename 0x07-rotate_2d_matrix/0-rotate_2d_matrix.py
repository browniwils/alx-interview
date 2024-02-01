#!/usr/bin/python3
"""2D matrix rotation module."""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place."""

    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return

    if not all(map(lambda x: type(x) == list, matrix)):
        return

    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return

    column = 0
    row = rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if row == -1:
            row = rows - 1
            column += 1
        matrix[-1].append(matrix[row][column])
        if column == cols - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
