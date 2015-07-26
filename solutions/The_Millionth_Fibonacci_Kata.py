"""
The Millionth Fibonacci Kata
http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""


def fib(n):
    """Calculates the nth Fibonacci number"""
    if n == 1 or n == 0:
        return n
    a, b = 0, 1
    if n > 1:
        while n > 2:
            a, b = b, a + b
            n -= 1
        return a + b
    else:
        while n < 0:
            a, b = b - a, a
            n += 1
        return a