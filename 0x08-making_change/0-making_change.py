#!/usr/bin/python3
"""
Coin Change Algorithm
"""

def makeChange(coin_values, target_amount):
    """
    Calculate the minimum number of coins needed to reach the target amount.
    
    Args:
        coin_values (list): Available coin denominations.
        target_amount (int): The desired total amount.
    
    Returns:
        int: Fewest number of coins needed, or -1 if not possible.
    """
    if target_amount <= 0:
        return 0

    coin_values.sort(reverse=True)
    remaining_amount, num_coins = target_amount, 0

    for coin in coin_values:
        while remaining_amount >= coin:
            remaining_amount -= coin
            num_coins += 1

    return num_coins if remaining_amount == 0 else -1
