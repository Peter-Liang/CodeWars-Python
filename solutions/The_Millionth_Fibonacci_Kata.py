"""
The Millionth Fibonacci Kata
http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""


def fib(n):
    """Calculates the nth Fibonacci number"""
    if n >= 0:
        return fibiter(1, 0, 0, 1, n)
    if n < 0:
        a, b = 0, 1
        for _ in xrange(0, n, -1):
            a, b = b - a, a
        return a


def fibiter(a, b, p, q, count):
    if count == 0:
        return b
    if count % 2 == 0:
        return fibiter(a, b, p * p + q * q, q * q + 2 * p * q, count / 2)
    else:
        return fibiter(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)