#!/usr/bin/python3
"""
Determines the minimum number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Find the fewest number of coins needed to achieve the total amount.
    Arguments:
        coins: List of integers representing coin denominations.
        total: The target amount to achieve.
    Returns:
        Fewest number of coins needed to meet total, or -1 if it is not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            num_coins += remaining // coin
            remaining %= coin

    return num_coins if remaining == 0 else -1
