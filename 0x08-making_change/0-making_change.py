#!/usr/bin/python3
"""function"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    """
    num = [float('inf')] * (total + 1)
    num[0] = 0
    if total <= 0:
        return 0
    for coin in coins:
        for i in range(coin, total + 1):
            num[i] = min(num[i], num[i - coin] + 1)
    if num[total] != float('inf'):
        return num[total]
    else:
        return -1
