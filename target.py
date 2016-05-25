#target.py
#this program draws an archery target
#by: Paul

from graphics import *

def main():
    win = GraphWin("Archery target",500,500)
    w = Circle(Point(250,250),200)
    w.setFill("white")
    w.draw(win)

    bc = Circle(Point(250,250),160)
    bc.setFill("black")
    bc.draw(win)

    bl = Circle(Point(250,250),120)
    bl.setFill("blue")
    bl.draw(win)

    r = Circle(Point(250,250),80)
    r.setFill("red")
    r.draw(win)

    y = Circle(Point(250,250),40)
    y.setFill("yellow")
    y.draw(win)

    c = Circle(Point(250,250),5)
    c.setFill("black")
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()

main()
