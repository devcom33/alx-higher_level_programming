"""A function that divides all elements of a matrix"""

def matrix_divided(matrix, div):

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
