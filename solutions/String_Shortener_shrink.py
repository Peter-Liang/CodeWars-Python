"""
String Shortener (shrink)
http://www.codewars.com/kata/557d18803802e873170000a0/train/python
"""


def shorten(string, length, glue="..."):
    if length >= len(string):
        return string
    if length == len(glue) + 1 or len(glue) > length:
        return string[:length]
    shortened = length - len(glue)
    return string[:int(shortened / 2)] + glue + string[-(int(shortened / 2) + (shortened % 2)):]