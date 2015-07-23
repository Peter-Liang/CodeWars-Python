"""
Calculator
http://www.codewars.com/kata/5235c913397cbf2508000048/train/python
"""
import operator


class Calculator(object):
    operands = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

    def __init__(self):
        self.result = []

    def evaluate(self, string):
        self.result = string.split(' ')
        self._loop('*/')
        self._loop('+-')
        return float(self.result[0])

    def _loop(self, operators):
        i = 1
        while i < len(self.result) - 1:
            if self.result[i] in operators:
                self.result[i - 1] = str(self.__class__.operands[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                self.result.pop(i + 1)
                self.result.pop(i)
                continue
            i += 1
