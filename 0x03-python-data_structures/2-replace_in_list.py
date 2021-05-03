#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx >= 0 and idx < n:
        my_list[idx] = element
    return my_list
