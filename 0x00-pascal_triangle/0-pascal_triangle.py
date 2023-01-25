#!/usr/bin/python3
"""
Print a pascal's triangle
"""

def pascal_triangle(n):
    """Function that returns a list of integers representing a pascal's
    triangle
    """
    list1 = []
    if n <= 0:
        return []
    for row in range(n):
        temp = []
        for column in range(row+1):
            if column == 0 or column == row:
                temp.append(1)
            else:
                temp.append(list1[row-1][column-1] + list1[row-1][column])
        list1.append(temp)
    return list1
