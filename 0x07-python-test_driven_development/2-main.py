#!/usr/bin/python3

matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix1 = [[3, 15, 90, 24], [24, 9, 3, 6], [3, 12, 15, 3], [9, 12, 18, 21]]


matrixa = matrix_divided(matrix1, 3)

print(matrixa)

matrix = [
        [1, 2, 3], 
        [4, 5, 6]
        ]
print(matrix_divided(matrix, 3))
print(matrix)
