#!/usr/bin/python
""" pascal triangle implementation """


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]
    i = 1

    while i < n:
        row = [1]
        m = 1
        while m < i:
            row.append(pascal[i-1][m] + pascal[i-1][m-1])
            m += 1

        row.append(1)
        pascal.append(row)
        i += 1
    return pascal
