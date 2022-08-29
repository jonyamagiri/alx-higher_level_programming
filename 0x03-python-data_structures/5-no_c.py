#!/usr/bin/python3
def no_c(my_string):
    new_string = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(new_string))
