#!/usr/bin/python3
from sys import argv

if len(argv) > 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)


def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i, x in enumerate(queens))


def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = [solution+[i+1]
                     for solution in solutions
                     for i in range(BOARD_SIZE)
                     if not under_attack(i+1, solution)]
    return solutions

if __name__ == '__main__':
    BOARD_SIZE = int(argv[1])
    for answer in solve(BOARD_SIZE):
        print(list([x-1, y-1] for x, y in enumerate(answer, start=1)))
