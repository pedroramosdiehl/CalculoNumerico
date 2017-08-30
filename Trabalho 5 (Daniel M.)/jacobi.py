import numpy as np


def multiply_matrix(A, B):
    if A.shape[1] != B.shape[0]:
        raise NameError('Not possible')

    C = np.zeros(shape=(A.shape[0], B.shape[1]))

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            for k in range(B.shape[0]):
                C[i, j] += A[i, k] * B[k, j]

    return C


def sum_matrix(A, B):
    if A.shape != B.shape:
        raise NameError('Matrix of different dimension')

    lines = A.shape[0]
    columns = A.shape[1]

    C = np.zeros(shape=(lines, columns))

    for i in range(lines):
        for j in range(columns):
            C[i, j] = A[i, j]+B[i, j]

    return C


def generate_matrix_c(A):
    dimension = A.shape[0]

    C = np.zeros(shape=(dimension, dimension))

    for i in range(dimension):
        for j in range(dimension):
            C[i, j] = 0 if i == j else -A[i, j] / A[i, i]

    return C


def generate_matrix_g(A, b):
    dimension = A.shape[0]

    g = np.zeros(shape=(dimension, 1))

    for i in range(dimension):
        g[i, 0] = b[i, 0] / A[i, i]

    return g


A = np.matrix('10. 2. 3.; 1. 5. 1.; 2. 3. 10.')
b = np.matrix('7.; -8.; 6.')

x = np.matrix('0.; 0.; 0.')
previous_x = np.matrix('1.; 1.; 1.')

C = generate_matrix_c(A)
g = generate_matrix_g(A, b)

e = 0.001

while abs(x[0, 0] - previous_x[0, 0]) > e:
    previous_x = x
    x = sum_matrix(multiply_matrix(C, previous_x), g)

print x
