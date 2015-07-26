"""
The Millionth Fibonacci Kata
http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""

cache = {0: 0, 1: 1}


def fib(n):
    """Calculates the nth Fibonacci number"""
    if n not in cache:
        if n > 0:
            maxkey, _ = max(cache.items())
            while maxkey < n:
                cache[maxkey + 1] = cache[maxkey - 1] + cache[maxkey]
                maxkey += 1
        else:
            minkey, _ = min(cache.items())
            while minkey > n:
                cache[minkey - 1] = cache[minkey + 1] - cache[minkey]
                minkey -= 1
    return cache[n]