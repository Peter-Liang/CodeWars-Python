"""
Square into Squares. Protect trees!

http://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

"""


def decompose(n, goal=None):
    if not goal:
        goal = n ** 2
    for i in range(n - 1, 0, -1):
        if goal > i ** 2:
            for j in range(i - 1, 0, -1):
                if i ** 2 + j ** 2 == goal:
                    return [j, i]
                result = decompose(j, goal - (i ** 2))
                if result:
                    result.append(i)
                    sorted(result)
                    return result
    return None