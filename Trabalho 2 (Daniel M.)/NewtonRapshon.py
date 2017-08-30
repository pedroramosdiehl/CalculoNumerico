from math import sqrt

def matrix_multiplication(matrix_a, matrix_b):
    """Docstring"""

    #Generalize this
    matrix_c = [[0.0,0.0],[0.0,0.0]]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_a[0])):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c

def matrix_inverse(matrix):
    """Docstring"""

    dimension = len(matrix)

    con = 0.0

    for k in range(dimension):
        con = matrix[k][k]
        matrix[k][k] = 1

        for j in range(dimension):
            matrix[k][j] = matrix[k][j]/con

        for i in range(dimension):
            if i != k:
                con = matrix[i][k]
                matrix[i][k] = 0.0

                for j in range(dimension):
                    matrix[i][j] -= matrix[k][j]*con

    return matrix

def matrix_jacobian(x1, x2):
    """Docstring"""

    matrix = [[0.0,0.0],[0.0,0.0]]

    matrix[0][0] = x2
    matrix[0][1] = x1
    matrix[1][0] = 2*x1
    matrix[1][1] = 2*x2

    return matrix

f = lambda x1,x2: x1*x2-1
g = lambda x1,x2: x1**2 + x2**2 - 4

e = 0.00001
iterations = 0
x1 = 1.8
x2 = 0.5

function_matrix = [[0.0],[0.0]]
delta_matrix = [[1.0],[1.0]]
jacob = [[0.0,0.0],[0.0,0.0]]

while sqrt(delta_matrix[0][0]**2 + delta_matrix[1][0]**2) > e:
    function_matrix[0][0] = -f(x1,x2)
    function_matrix[1][0] = -g(x1,x2)

    jacob = matrix_jacobian(x1, x2)
    delta_matrix = matrix_multiplication(matrix_inverse(jacob), function_matrix)

    x1 += delta_matrix[0][0]
    x2 += delta_matrix[1][0]

    iterations += 1

print 'x1 = ',x1
print 'x2 = ', x2
print 'iterations = ', iterations
