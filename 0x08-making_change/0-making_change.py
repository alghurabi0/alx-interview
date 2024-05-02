#!/usr/bin/python3
"""making change coin problem"""


def makeChange(coins, total):
    """ make change coin problem """
    if total <= 0:
        return 0
    coins.sort()
    n = len(coins)
    i = n - 1
    ans = 0

    while i >= 0:
        while total >= coins[i]:
            total -= coins[i]
            ans += 1
        i -= 1

    if total != 0:
        return -1
    return ans
