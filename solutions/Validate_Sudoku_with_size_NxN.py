"""
Validate Sudoku with size `NxN`
http://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
"""
from math import sqrt


class Sudoku(object):
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.n = 0
        self.block_len = 0

    def is_valid(self):
        self.n = len(self.sudoku)
        try:
            self.block_len = int(sqrt(self.n))
        except ValueError:
            return False
        if any([len(row) != self.n for row in self.sudoku]):
            return False
        return all([self._is_valid_row(i)
                    and self._is_valid_column(i)
                    and self._is_valid_block(i)
                    for i in range(self.n)])

    def _is_valid_row(self, row_num):
        return self._is_valid_set(set(self.sudoku[row_num]))

    def _is_valid_column(self, column_num):
        return self._is_valid_set(set([self.sudoku[r][column_num] for r in range(self.n)]))

    def _is_valid_block(self, block_num):
        block_row_num, block_column_num = divmod(block_num, self.block_len)
        block_row, block_column = block_row_num * self.block_len, block_column_num * self.block_len
        block_set = set()
        for r in range(block_row, block_row + self.block_len):
            for c in range(block_column, block_column + self.block_len):
                block_set.add(self.sudoku[r][c])
        return self._is_valid_set(block_set)

    def _is_valid_set(self, num_set):
        return len(num_set) == self.n \
               and max(num_set) == self.n \
               and min(num_set) == 1 \
               and all(type(i) is int for i in num_set)