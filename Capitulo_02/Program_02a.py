# Program 02a: A simple separable ODE. See Example 1.
from sympy import dsolve, Eq, Function, symbols
t = symbols('t')
x = symbols('x', cls=Function)
sol = dsolve(Eq(x(t).diff(t), -t/x(t)), x(t))
print(sol)