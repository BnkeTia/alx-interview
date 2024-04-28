#!/bin/python3
"""A function that returns the list of integers representing the
pascals triangle
"""


def pascal_triangle(n):
    """A module that returns a list of integers."""

    
    # initialize list
    triangle = []
    # check if n is zero or negative number
    if n <= 0:
        return triangle

    # iterate through n initialize list to store number
    for i in range(n):
        row = []

        # iterate through previous loop.
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)

            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # add sum to the triangle
        triangle.append(row)

    return triangle
