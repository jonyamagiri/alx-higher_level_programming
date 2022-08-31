#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_my_list = my_list[:]  # Equivalent to list.copy()
    for index, elem in enumerate(copy_my_list):
        if elem == search:
            copy_my_list[index] = replace
    return copy_my_list
