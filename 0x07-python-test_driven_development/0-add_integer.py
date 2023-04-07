#!/usr/bin/python3
"""
    Module that add 2 integers
"""

def add_integer(a, b=98):
    """
    Function to add 2 integers
    a and b must be integers or floats
    Otherwise raise a TypeError exception with the message
    a must be an integer or b must be an integer

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        a + b (int): Sum of the two integers

    Raises:
        TypeError: If a or b is not an integer

    Samples:
        >>> add_integer(22)
        120

        >>> add_integer(22, 21)
        43

        >>> add_integer("a")
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer

        >>> add_integer(2.87, 3)
        5.87

        >>> add_integer(0, 0)
        0
    """
    if not isinstance (a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance (b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
