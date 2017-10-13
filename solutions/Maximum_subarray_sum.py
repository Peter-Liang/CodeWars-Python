"""
5 kyu: Maximum subarray sum
http://www.codewars.com/kata/maximum-subarray-sum/train/python

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def maxSequence(arr):
    maximum = 0
    local_maximum = 0
    for i in arr:
        if local_maximum > 0:
            local_maximum += i
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
        elif i > 0:
            local_maximum += i

    return maximum


assert maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
