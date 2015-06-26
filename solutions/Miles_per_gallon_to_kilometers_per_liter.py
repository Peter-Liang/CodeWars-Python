"""
Miles per gallon to kilometers per liter
http://www.codewars.com/kata/557b5e0bddf29d861400005d/train/python
"""


def converter(mpg):
    return float("{0:.2f}".format(mpg / 4.54609188 * 1.609344))