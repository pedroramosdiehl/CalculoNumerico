from math import log10 as log
from math import fabs as absolute

def function(n):
    return n * log(n) - 1

a = 2.0
b = 3.0
x = 0.0
cont = 0
e = 0.0001

while absolute(a-b) > e:
    x = (a+b)/2

    if function(a)*function(x) < 0:
        b = x
    else:
        a = x
        
    cont += 1

print "Numero de interacoes",cont
print x
