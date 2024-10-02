#!/usr/bin/python3
"""function that change comes from within"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    """
    nums = [float('inf')] * (total + 1)
    nums[0] = 0
    if total <= 0:
        return 0
    for coin in coins:
        for i in range(coin, total + 1):
            nums[i] = min(nums[i], nums[i - coin] + 1)
    if nums[total] != float('inf'):
        return nums[total]
    else:
        return -1
