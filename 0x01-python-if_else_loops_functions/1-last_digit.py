#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = number < 0
last = abs(number) % 10
last = -last if neg else last
val = "Last digit of {} is {} ".format(number, last)
if last > 5:
    val += "and is greater than 5"
elif last == 0:
    val += "and is 0"
else:
    val += "and is less than 6 and not 0"
print(val)
