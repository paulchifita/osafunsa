#arrow_fractal
#by Paul Chifita

from graphics import *
from turtle import Turtle
from math import sqrt

        
def Arrow(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        length1 = length / 3
        level1 = level - 1
        turtle.turn(60)
        Worra(turtle, length1, level1)
        turtle.turn(-60)
        Arrow(turtle, length1, level1)
        turtle.turn(-60)
        Worra(turtle, length1, level1)
        turtle.turn(60)

        
      

def Worra(turtle, length, level):
    if level == 0:
        turtle.move(length)
    else:
        length1 = length / 3
        level1 = level - 1
        turtle.turn(-60)
        Arrow(turtle, length1, level1)
        turtle.turn(60)
        Worra(turtle, length1, level1)
        turtle.turn(60)
        Arrow(turtle, length1, level1)
        turtle.turn(-60)

     

def main():
    print("Arrow Fractal")
    win = GraphWin("Arrow Fractal",800, 800)
    win.setCoords(0,0, 500, 500)
    win.setBackground("green")
    t = Turtle(win, Point(125,250))
    level = eval(input("What level do you want? "))
    Arrow(t, 300, level)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
