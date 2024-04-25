#!/usr/bin/python3
"""rotate matrix 90 degree"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    mat = []
    for i in range(0, len(matrix[0])):
        row = []
        for j in range(len(matrix)-1, -1, -1):
            row.append(matrix[j][i])
        mat.append(row)
    print(mat)
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix[j])):
            matrix[j][i] = mat[j][i]
