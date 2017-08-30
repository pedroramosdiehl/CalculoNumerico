import numpy as np
#import time

A = np.matrix('1 2 -2 1; 2 5 -2 3; -2 -2 5 3; 1 3 3 2')
b = np.matrix('4; 7; -1; 0')

def lu_decomposition(A):
    # if A.shape[0]!=A.shape[1]: implement exception

    dimension = A.shape[0]

    L = np.zeros(shape=(dimension,dimension))
    U = np.zeros(shape=(dimension,dimension))

    for i in range(dimension):
        L[i,i] = 1.0

    for i in range(dimension):
        for j in range(dimension):
            sum = 0.0

            if j >= i:
                for k in range(i+1):
                    sum += L[i,k] * U[k,j]

                U[i,j] = A[i,j] - sum
            else:
                for k in range(j+1):
                    sum += L[i,k] * U[k,j]

                L[i,j] = (A[i,j] - sum)/U[j,j]

    return L,U

def solveReverse(L, b):
    dimension = L.shape[0]

    y = np.zeros(shape = (dimension,1))

    for i in range(dimension):
        sum = 0

        for j in range(dimension):
            if j<i:
                sum += L[i][j]*y[j]

        y[i] = b[i] - sum

    return y

def solveNormal(U,y):
    dimension = U.shape[0]

    x = np.zeros(shape = (dimension,1))

    for i in range(dimension-1,-1,-1): #range([start], stop[, step])
        sum = 0

        for j in range(0,dimension):
            if not(j == i):
                sum += U[i][j] * x[j]

        x[i] = (y[i] - sum)/ U[i][i]

    return x

#a=time.clock()

l,u = lu_decomposition(A)
y = solveReverse(l,b)
x = solveNormal(u,y)

#b = time.clock()

print "matriz L \n",l
print "matriz U \n",u
print "L * U \n",np.dot(l,u)
print "\nvetor y \n",y
print "\nvetor x \n",x

#print 'delta', b-a
