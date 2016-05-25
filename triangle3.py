#triangle3.py
#This program uses functions to draw a triangle so that its area and perimeter can be calculated and displayed
#by Paul Chifita

import math
from graphics import*

def square(x):
    return x*x

def distance(p1,p2):
    dist = math.sqrt(square(p2.getX()-p1.getX())+square(p2.getY()-p1.getY()))
    return dist

def triArea(a,b,c):
     
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    win = GraphWin("Drawing a triangle so that its area and perimeter can be calculated and displayed",600,600) 
    win.setCoords(0,0,10,10)
    win.setBackground("yellow")
    d = Rectangle(Point(0,-1),Point(11,1.2))
    d.setFill("grey")
    d.draw(win)
    message = Text(Point(5,0.8),"Click on three points to draw a triangle")
    message.setStyle("bold")
    message.setFill("blue")
    message.setSize(12)
    message.draw(win)
    m = Text(Point(5,0.3),"Use as much as you want of the yellow space")
    m.setStyle("bold")
    m.draw(win)
    
    #Get and draw vertices of the triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use the polygon object to draw the triangle
    tri = Polygon(p1,p2,p3)
    tri.setWidth(3)
    tri.setFill("beige")
    tri.draw(win)

    #define a,b,c and s to use for calculating the triangle area
    a = distance(p1,p2)
    b = distance(p2,p3)
    c = distance(p1,p3)
 
    #calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    area = triArea(a,b,c)
    message.setText("The perimeter is: {0:0.2f}".format(perim)+" pixels, while the area is: {0:0.2f}".format(area)+" pixels squared")
    m.setText("Click inside the triangle to close window!")

    #wait for another click to exit
    win.getMouse()
    win.close()

main()
