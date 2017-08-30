import numpy as np
import algebra


def multiply_matrix(A, B):
    if A.shape[1] != B.shape[0]:
        raise NameError('deu ruim')

    C = np.zeros(shape=(A.shape[0], B.shape[1]))

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            for k in range(B.shape[0]):
                C[i, j] += A[i, k] * B[k, j]

    return C


def transpose_matrix(A):
    t = np.zeros(shape=(A.shape[1], A.shape[0]))

    for i in range(t.shape[0]):
        for j in range(t.shape[1]):
            t[i, j] = A[j, i]

    return t


def generate_A(points):
    A = np.zeros(shape=(len(points), k + 1))

    for i, point in enumerate(points):
        for j in range(k + 1):
            A[i, j] = point[0] ** abs(k - j)

    return A


def generate_b(points):
    b = np.zeros(shape=(len(points), 1))

    for i, point in enumerate(points):
        b[i, 0] = point[1]

    return b


if __name__ == '__main__':
    points_list = [(-2., -3.), (-1., 0.), (1., 0.), (2., -3.), (2., -1.), (4., 0.), (5., 2.)]
    # points_list = [(-2., 0.), (-1., 4.), (0., 5.), (1., 4.), (2., 0.)] # ex 1
    # points_list = [(-4, 0), (3, 0), (0, 0), (-3, -576), (4, -576), (-1, 144), (2, 144)] # ex 2
    # points_list = [(0., 1.), (2., 1.), (2., 5.), (6., 2.), (6., 4.), (6., 6.)] # ex 3

    k = 3  # ax3+bx2+cx1+d=y
    # k = 4
    # k = 6
    # k = 2

    A = generate_A(points_list)
    b = generate_b(points_list)
    print A
    print b

    At = transpose_matrix(A)

    An = multiply_matrix(At, A)
    bn = multiply_matrix(At, b)
    # An = At.dot(A)
    # bn = At.dot(b)

    print An
    print bn

    solver = algebra.Algebra()

    print solver.solve_system(An, bn)
