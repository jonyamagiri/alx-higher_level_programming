#!/usr/bin/python3
"""
Module 100-my_int.py with class MyInt that inherits class int.
Has == and != operators inverted.
"""


class MyInt(int):
    """
    Defines class MyInt that inherits class int.
    Inverts the int operators == and !=.
    Methods:
        __init__(self, value)
        __eq__(self, value)
        __ne__(self, value)
    """

    def __init__(self, value):
        """Initializes value"""
        self.value = value

    def __eq__(self, value):
        """Invert self==value operator with self!=value"""
        return self.value != value

    def __ne__(self, value):
        """Invert self!=value operator with self==value"""
        return self.value == value
