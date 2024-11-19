#!/usr/bin/python3
"""
Defines a function to generate Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: Pascal's Triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Fill in the middle values as the sum of two elements from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with a 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle

