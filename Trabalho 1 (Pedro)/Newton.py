from math import fabs as absolute
from math import log10 as log

def function(n):
    return ( n * log(n)  )- 1

def derivative(n):
    p = 0.000000000001 #10^-12
    return ( function(n+p) - function(n) ) / p

x0 = 3.0
x1 = 0.0
e = 0.0001
cont = 0

while True:
    cont += 1
    x1 = x0 - ( function(x0) / derivative(x0) )

    if absolute(x0 - x1) < e:
        x0 = x1
        break

    x0 = x1

print "Numero de interacoes",cont
print x0
