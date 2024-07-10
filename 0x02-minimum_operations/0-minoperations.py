#!/usr/bin/python3
"""function """


def minOperations(n: int) -> int:
    """
    returns an integer

    Args:
        n(int): numbers
    Returns:
        int: number of operations needed to result
    """
    if n <= 0:
        return 0
    num = [float('inf')] * (n + 1)
    num[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                num[i] = min(num[i], num[j] + (i // j))

    return num[n]
