#!/usr/bin/python3
"""
Module documentation for 0-making)change.py
"""


def makeChange(coins, total):
    """
    A function that  determine the fewest number
    of coins needed to meet a given amount
    """
    if total < 1:
        return 0
    coins = sorted(coins, reverse=True)
    coin_sum = 0
    count = 0

    for coin in coins:
        while coin + coin_sum <= total:
            coin_sum += coin
            count += 1
        if coin_sum == total:
            return count
    if coin_sum == total:
        return count
    return -1
