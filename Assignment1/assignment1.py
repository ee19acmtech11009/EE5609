#EE5609:Matrix Theory
#Assignment 1
#Lines and Planes(Prob.39)
#Code by Sneha Konduru
#Roll no: ee19acmtech11009


#Libraries
from sympy import *
from sympy.abc import x, h
from sympy import Point, solve, Eq
from sympy.geometry import Line
from sympy import Derivative
from fractions import Fraction 


 
#Given points   
p1, p2 = Point(h, 3), Point(4, 1)

#Given Line equation arranged in the form of y=mx+c
y=Fraction(7,9)*x-Fraction(19,9)

#Line joining P1 and P2
l1 = Line(p1, p2)

#Slope of line joining P1 and P2
slope1=l1.slope

#Slope of given line equation
slope2=diff(y,x)

print("slope of line intersecting 2 points :",slope1)
print("slope of the line 7x-9y-19 :",slope2)

#Equating slope1*slope2= -1 (given lines intersect perpendicularly)
eq1 = Eq(slope1*slope2+1)
h = solve(eq1)

print("value of h:",h)


  


