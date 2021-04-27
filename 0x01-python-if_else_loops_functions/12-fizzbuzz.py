#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        displayed = False
        if i % 3 == 0:
            print("Fizz", end="")
            displayed = True
        if i % 5 == 0:
            print("Buzz", end="")
            displayed = True
        if not displayed:
            print(i, end="")
        print(" ", end="")
