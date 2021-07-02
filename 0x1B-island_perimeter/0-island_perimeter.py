#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """Get the perimeter of the island"""
    rows = len(grid)
    cols = len(grid[0])

    total = 0  # total island perimeter

    def getUp(row, col):
        """check if upwards is water/zero"""
        if row - 1 < 0:
            return 1
        return 1 - grid[row-1][col]

    def getDown(row, col):
        """check if downwards is water/zero"""
        if row + 1 >= rows:
            return 1
        return 1 - grid[row+1][col]

    def getRight(row, col):
        """check if right is water/zero"""
        if col + 1 >= cols:
            return 1
        return 1 - grid[row][col+1]

    def getLeft(row, col):
        """check if left is water/zero"""
        if col - 1 < 0:
            return 1
        return 1 - grid[row][col-1]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                total += getUp(row, col)
                total += getDown(row, col)
                total += getRight(row, col)
                total += getLeft(row, col)

    return total
