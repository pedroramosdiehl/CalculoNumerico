import numpy as np


class Algebra:
    def lu_decomposition(self, A):
        if A.shape[0] != A.shape[1]:
            raise

        dimension = A.shape[0]

        L = np.zeros(shape=(dimension, dimension))
        U = np.zeros(shape=(dimension, dimension))

        for i in range(dimension):
            L[i, i] = 1.0

        for i in range(dimension):
            for j in range(dimension):
                sum = 0.0

                if j >= i:
                    for k in range(i + 1):
                        sum += L[i, k] * U[k, j]

                    U[i, j] = A[i, j] - sum
                else:
                    for k in range(j + 1):
                        sum += L[i, k] * U[k, j]

                    L[i, j] = (A[i, j] - sum) / U[j, j]

        return L, U

    def solve_reverse(self, L, b):
        dimension = L.shape[0]

        y = np.zeros(shape=(dimension, 1))

        for i in range(dimension):
            sum = 0

            for j in range(dimension):
                if j < i:
                    sum += L[i][j] * y[j]

            y[i] = b[i] - sum

        return y

    def solve_normal(self, U, y):
        dimension = U.shape[0]

        x = np.zeros(shape=(dimension, 1))

        for i in range(dimension - 1, -1, -1):  # range([start], stop[, step])
            sum = 0

            for j in range(0, dimension):
                if not(j == i):
                    sum += U[i][j] * x[j]

            x[i] = (y[i] - sum) / U[i][i]

        return x

    def solve_system(self, A, b):
        l, u = self.lu_decomposition(A)
        y = self.solve_reverse(l, b)
        x = self.solve_normal(u, y)

        return x
