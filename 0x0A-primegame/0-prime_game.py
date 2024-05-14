#!/usr/bin/python3
""" prime game """


def isWinner(x, nums):
    """ prime game """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    male = 0
    female = 0

    c = [1 for x in range(sorted(nums)[-1] + 1)]
    c[0], c[1] = 0, 0
    for i in range(2, len(c)):
        rm_multiples(c, i)

    for i in nums:
        if sum(c[0:i + 1]) % 2 == 0:
            male += 1
        else:
            female += 1
    if male > female:
        return "Ben"
    if female > male:
        return "Maria"
    return None


def rm_multiples(nums1, s):
    """ rm multiples """
    for a in range(2, len(nums1)):
        try:
            nums1[a * s] = 0
        except (ValueError, IndexError):
            break
