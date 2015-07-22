"""
Battleship field validator
http://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""


def validateBattlefield(field):
    ships = {}
    for row in range(len(field[0])):
        for col in range(len(field)):
            if field[row][col] == 1:
                try:
                    result = getShipSize(row, col, field)
                    ships[result] = ships.get(result, 0) + 1
                except ValueError:
                    return False
    return ships.get(4, 0) == 1 and ships.get(3, 0) == 2 and ships.get(2, 0) == 3 and ships.get(1, 0) == 4


def isCornerValid(row, col, field):
    if row == len(field) - 1:
        return True
    if col == 0:
        return field[row + 1][col + 1] != 1
    if col == len(field[0]) - 1:
        return field[row + 1][col - 1] != 1
    return field[row + 1][col + 1] != 1 and field[row + 1][col - 1] != 1


def isSideValid(row, col, field):
    if row == len(field) - 1 or col == len(field[0]) - 1:
        return True
    return not (field[row + 1][col] != 0 and field[row][col + 1] != 0)


def isValidPoint(row, col, field):
    return isCornerValid(row, col, field) and isSideValid(row, col, field)


def getShipSize(row, col, field):
    if not isValidPoint(row, col, field):
        raise ValueError('Invalid disposition')
    field[row][col] = -1
    if row != len(field) and field[row + 1][col] == 1:
        return 1 + getShipSize(row + 1, col, field)
    if col != len(field[0]) and field[row][col + 1] == 1:
        return 1 + getShipSize(row, col + 1, field)
    return 1