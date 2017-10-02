"""
6 kyu: Consecutive strings
http://www.codewars.com/kata/consecutive-strings/train/python

You are given an array strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i

    return ''.join(strarr[index: index + k])


assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
