#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows (n).

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists, where each sublist represents a row of Pascal's triangle.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [
            1 if j == 0 or j == i else triangle[i - 1][j - 1] + triangle[i - 1][j]
            for j in range(i + 1)
        ]
        triangle.append(row)

    return triangle

