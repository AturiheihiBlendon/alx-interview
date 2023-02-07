#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    returns the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if (n < 2):
        return 0

    operations= 0
    iterations = 2

    while iterations <= n:
        if n % iterations == 0:
            operations += iterations
            n = n / iterations
            iterations -= 1
        iterations += 1
    return operations
