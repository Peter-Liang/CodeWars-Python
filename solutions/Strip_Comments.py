"""
Strip Comments

http://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
"""


def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)
