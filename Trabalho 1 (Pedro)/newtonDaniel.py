from math import fabs as absolute
from math import log10 as log

def function(n):
    return ( n * log(n)  )- 1

def derivative(n):
    p = 0.000000000001
    return ( function(n+p) - function(n) ) / p

x0 = 3.0
x1 = 0.0
e = 0.00001
cont = 0
buff = x0

while not absolute(buff - x1) < e:
    cont += 1
    x1 = x0 - ( function(x0) / derivative(x0) )
    buff = x0
    x0 = x1

print(cont)
print(x0)
