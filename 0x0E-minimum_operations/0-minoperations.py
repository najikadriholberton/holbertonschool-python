#!/usr/bin/python3
"""Minimum Operation Module"""


def minOperations(n):
    """try to find the minimum operations needed"""
    if n <= 1:
        return 0
    m = n
    div = 2
    min_op = 0
    while m > 1:
        if m % div == 0:
            m /= div
            min_op += div
        else:
            div += 1
    return min_op
