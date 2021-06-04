#!/usr/bin/python3
"""Find peak in an unsorted list"""


def find_peak(list_of_integers):
    """Find the peak in the list of integers"""
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]

    h = n-1
    l = 0
    li = list_of_integers
    while h > l:
        m = (h + l) // 2
        if li[m] <= li[m+1]:
            l = m + 1
        elif li[m] <= li[m-1]:
            h = m - 1
        elif li[m] >= li[m+1] and li[m] >= li[m-1]:
            return li[m]
    return li[l]
