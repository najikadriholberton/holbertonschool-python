#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op not in '+-*/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if op == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif op == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif op == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif op == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
