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
    i, j = 0, 2

    while n > 1:
        while n % j == 0:
            i += j
            n //= j
        j += 1

    return i
