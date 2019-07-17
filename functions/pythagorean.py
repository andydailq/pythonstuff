"""
File: pythagorean.py
-------------------------
This file should implement a console program that calculates
the length of the hypotenuse of a right triangle using the
Pythagorean theorem.
"""

import math


def pythag(a, b):
    """
    This function takes in the two non-hypotenuse sides
    of a right triangle (a and b) and calculates and
    returns the length of the hypotenuse. The inputs are
    the two side lengths that are orthogonal to each other
    and the output is a third value that measures the hypotenuse
    >>> pythag(3,4)
    5.0
    >>> pythag(5,12)
    13.0
    >>> pythag(0,0)
    0.0
    >>> pythag(0,2)
    2.0
    >>> pythag(0,5)
    5.0
    """
    c = math.sqrt(a*a + b*b)
    return c

def main():
    """
    This program calculates the hypotenuse
    of any given right triangle assuming only
    positive inputs. The inputs and outputs are
    the same for the pythag() function.
    """
    print("Enter values to compute the Pythagorean theorem.")
    a = float(input("a: "))
    b = float(input("b: "))
    c = pythag(a, b)
    print("c: " + str(c))


if __name__ == "__main__":
    main()
