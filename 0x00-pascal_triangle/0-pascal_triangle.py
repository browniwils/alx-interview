#!/usr/bin/python3
"""Module for initiating pascal triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing 
    the Pascal’s triangle."""
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)

    return pascal