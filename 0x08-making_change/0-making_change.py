#!/usr/bin/python3
"""Module for making change."""


def makeChange(coins, total):
    """Checks and determine fewest number of coin
    needed to sums up to get the total.
    """

    if total <= 0:
        return 0

    i = total
    coins_count = 0
    coin_index = 0

    coins_stored = sorted(coins, reverse=True)
    number_of_coins = len(coins)

    while i > 0:
        if coin_index >= number_of_coins:
            return -1
        if i - coins_stored[coin_index] >= 0:
            i -= coins_stored[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count
