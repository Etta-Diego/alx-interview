Pascal's Triangle in Python
Description
This directory contains a Python function that generates Pascal's Triangle for a given number of rows, n. Pascal’s Triangle is a triangular array where each number is the sum of the two numbers directly above it. This project demonstrates the creation of a function that returns a list of lists of integers, representing the rows of Pascal’s Triangle.

Files
0-pascal_triangle.py: This file contains the implementation of the pascal_triangle(n) function.
0-main.py: A test file that imports the pascal_triangle function and prints Pascal's Triangle for a sample input (in this case, n = 5).
Function Details
def pascal_triangle(n):
Arguments:
n (integer): The number of rows of Pascal's Triangle to generate.
Returns:
A list of lists, where each sublist represents a row of Pascal’s Triangle.
If n <= 0, the function returns an empty list.
Assumptions:
n is always a non-negative integer.

