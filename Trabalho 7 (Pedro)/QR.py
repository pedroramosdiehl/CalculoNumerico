import numpy as np
from math import sqrt


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


def sumDiagonalMatrix(A):
    sum = 0

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i > j:
                sum += A[i, j]

    return sum


def obtain(A, q, p):
    UL = np.identity(A.shape[0])

    UL[q, q] = UL[p, p] = A[p, p] / sqrt(A[p, p] ** 2 + A[q, p] ** 2)
    UL[p, q] = A[q, p] / sqrt(A[p, p] ** 2 + A[q, p] ** 2)
    UL[q, p] = -A[q, p] / sqrt(A[p, p] ** 2 + A[q, p] ** 2)

    return UL


def decompor(A):
    Q = np.identity(A.shape[0])
    R = np.identity(A.shape[0])

    UK = np.identity(A.shape[0])
    UL = np.identity(A.shape[0])

    for i in range(1, A.shape[0]):
        for j in range(0, i):
            UL = obtain(A, i, j)
            Q = multiply_matrix(Q, transpose_matrix(UL))
            UK = multiply_matrix(UL, UK)

    R = multiply_matrix(UK, A)

    return Q, R


if __name__ == '__main__':
    A = np.matrix('5 2 1; 2 3 1; 1 1 1')
    matrixList = []
    cont = 0

    e = 0.001

    print "Matriz A antes: \n",A

    while sumDiagonalMatrix(A) > e:
        Q, R = decompor(A)

        A = multiply_matrix(R, Q)
        matrixList.append(A)
        cont += 1

    # print matrixList,"\n"
    np.set_printoptions(precision=3, suppress=True)
    print "Matriz A depois: \n",(A)
    print "Auto Valores: \n","{",A[0, 0],",",A[1, 1],",",A[2,2],"}"
    print "Numero de iteracoes: ",cont
