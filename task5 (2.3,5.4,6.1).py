from sympy import *
import math
x,y,z,n=symbols("x y z n")



#2.3
var('i,j,n')
print(Sum(1/n),( n, 1, oo).evalf())

#5.4
print(solveset(Eq(x**7+7*x**5+3*x**4+5*x**3+26*x**2-10*x+40, 0), x).evalf())

#6.1
p1=plot(x**3/2 + 1 - cos(2-x),(x,-2*pi/3,pi))
