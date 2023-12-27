#!/usr/bin/python3
"""Minimum operation module."""


def minOperations(n: int) -> int:
    """
    Determine the minimum opeartions for running
    Args:
        n (int):
    Returns:
        Returns an int
    """
    if not isinstance(n, int):
        raise TypeError('Expected an integer')
    if n < 2:
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1
    return operations
