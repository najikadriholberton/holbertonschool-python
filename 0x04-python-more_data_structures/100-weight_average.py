#!/usr/bin/python3
def weight_average(my_list):
    total_weight = 0
    total = 0
    for score, weight in my_list:
        total += (score * weight)
        total_weight += weight
    return total / total_weight
