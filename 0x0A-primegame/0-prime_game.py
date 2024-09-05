#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None

    max_nums = max(nums)

    sieve = [True] * (max_nums + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_nums**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_nums + 1, i):
                sieve[multiple] = False

    prime_count_up_to = [0] * (max_nums + 1)
    count = 0
    for i in range(2, max_nums + 1):
        if sieve[i]:
            count += 1
        prime_count_up_to[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count_up_to[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
