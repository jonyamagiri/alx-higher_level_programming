#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    sum_weighted_scores = 0
    sum_weights = 0

# my_list has tuples [(item-0, item-1), (score, weight)]

    for item in my_list:
        sum_weighted_scores += (item[0] * item[1])
        sum_weights += item[1]
    return sum_weighted_scores / sum_weights
