#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows (n).

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists, where each sublist represents a row of Pascal's triangle.
    """
    triangle = []  # Initialize an empty list to store the rows of Pascal's triangle.

    # If n is less than or equal to 0, return an empty list.
    if n <= 0:
        return triangle

    # Loop to generate each row of the triangle.
    for i in range(n):
        row = []  # Initialize a new list to store the current row.
        
        # Populate the current row.
        for j in range(i + 1):
            # The first and last element of each row are always 1.
            if j == 0 or j == i:
                row.append(1)
            else:
                # Other elements are the sum of the two elements directly above them.
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # Append the completed row to the triangle.
        triangle.append(row)

    return triangle
