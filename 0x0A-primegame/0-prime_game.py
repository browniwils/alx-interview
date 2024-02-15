#!/usr/bin/python3
"""Module for prime game."""


def isWinner(x, nums):
    """Determines a winner in the prime game."""

    if x < 1:
        return None
    if not nums:
        return None

    player_one = {"name": "Maria", "won": 0}
    player_two = {"name": "Ben", "won": 0}

    max_num = max(nums)
    all_num = [True for x in range(1, max_num + 1, 1)]
    all_num[0] = False

    for idx, prime_num in enumerate(all_num, 1):
        if idx == 1:
            continue
        if not prime_num:
            continue
        for i in range(idx + idx, max_num + 1, idx):
            all_num[i - 1] = False

    for i, j in zip(range(x), nums):
        num_of_primes = len(list(filter(lambda x: x, all_num[0:j])))
        player_two["won"] += num_of_primes % 2 == 0
        player_one["won"] += num_of_primes % 2 == 1

    if player_one["won"] == player_two["won"]:
        return None
    if player_one["won"] > player_two["won"]:
        wins = player_one["name"]
    else: 
        wins = player_two["name"]
    return wins
