#Example 9. Write a Python program that plots a Sierpinski triangle fractal.
# A program that plots the Sierpinski fractal.
# Save file as sierpinski.py.
# Remember to run the Module (or type F5).
from turtle import *
def sierpinski(length, level): # Sierpinski function.
    speed(0) # Fastest speed.
    if level==0:
        return
    begin_fill() # Fill shape.
    color('red')
    
    for i in range(3):
        sierpinski(length/2, level-1)
        fd(length)
        lt(120)
    end_fill()

#Ejecutar >>> sierpinski(200, 4)