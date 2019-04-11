#Example 8. Write a Python program that plots a Koch square fractal curve
# A program for plotting a Koch square curve.
# Save file as koch_square.py.
# Remember to run the Module (or type F5).
from turtle import *
def koch_square(length, level): # Koch square function.
    speed(0) # Fastest speed.
    for i in range(4):
        plot_side(length, level)
        rt(90)

def plot_side(length, level): # Plot side function.
    if level==0:
        fd(length)
        return
    plot_side(length/3, level - 1)
    lt(90)
    plot_side(length/3, level - 1)
    rt(90)
    plot_side(length/3, level - 1)
    rt(90)
    plot_side(length/3, level - 1)
    lt(90)
    plot_side(length/3, level - 1)

#Ejecutar >>> koch_square(200, 4)