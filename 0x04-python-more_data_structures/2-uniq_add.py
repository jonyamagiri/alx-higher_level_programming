#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for integer in set(my_list):
        sum += integer
    return sum
