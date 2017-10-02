"""
7 kyu: Sum of odd numbers
http://www.codewars.com/kata/sum-of-odd-numbers/train/python
"""


def row_sum_odd_numbers(n):
    start = n ** 2 - (n - 1)
    return sum(range(start, start + n * 2, 2))


assert row_sum_odd_numbers(1) == 1
assert row_sum_odd_numbers(2) == 8
assert row_sum_odd_numbers(41) == 68921
