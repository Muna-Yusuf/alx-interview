#!/usr/bin/python3
"""Determine the winner of x rounds of a prime-number-based game.

    Parameters:
    x (int): The number of game rounds.
    nums (list): A list of integers, each representing the maximum
                 number in the set for each round.

    Returns:
    str: The name of the player with the most wins ('Maria' or 'Ben').
         If there is no clear winner, return None."""


def isWinner(x, nums):
    """Prime game winner."""
    if x < 1 or not nums:
        return None

    m_wins = 0
    b_wins = 0
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(n**0.5) + 1):
        if primes[x]:
            for y in range(x**2, n + 1, x):
                primes[y] = False

    for n in nums:
        count = sum(primes[2:n+1])
        b_wins += count % 2 == 0
        m_wins += count % 2 == 1

    if m_wins == b_wins:
        return None

    return 'Maria' if m_wins > b_wins else 'Ben'
