# Program 02b: The logistic equation. See Example 3.
from sympy import dsolve, Eq, Function, symbols
t = symbols('t')
a = symbols('a')
b=symbols('b')
P=symbols('P', cls=Function)
sol=dsolve(Eq(P(t).diff(t), P(t)*(a - b * P(t))), P(t))
print(sol)