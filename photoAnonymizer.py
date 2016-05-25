#photoAnonymizer.py
#this program draws faces over peoples' faces in the picture
#by: Paul Chifita

from graphics import*
import math

def pictureWindow(imageFile):
    img = Image(Point(0,0),imageFile)
    height = img.getHeight()
    width = img.getWidth()

    win = GraphWin(imageFile,width,height)
    img.move(width/2,height/2)
    img.draw(win)
    return win

def drawFace(c,radius,win):
    head = Circle(c,radius)
    head.setFill("white")
    head.draw(win)
    return head
    
def main():
     #Get filename from user
    win = GraphWin("Inputs window",400,200)
    win.setCoords(0,0,10,10)
    
    m = Text(Point(5,7),"Enter filename in the box below")
    m.draw(win)
    output = Entry(Point(5,5),20)
    output.draw(win)

    boxbut = Rectangle(Point(1.5,2.5),Point(8.5,3.5))
    boxbut.setFill("grey")
    boxbut.setOutline("black")
    boxbut.setWidth(5)
    boxbut.draw(win)
    button = Text(Point(5,3),"Click here to read file")
    button.setStyle("bold")
    button.setFill("red")
    button.setSize(12)
    button.draw(win)
   
    win.getMouse()
    filename = output.getText()
    m.setText("How many faces do you want to cover? ")
    button.setText("Click to start covering the faces")
    output.setText("")
    win.getMouse()
    nFace = eval(output.getText())
    win.close()
    
    
    win = pictureWindow(filename)
    
    for i in range(nFace):
        
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)

        line = Line(p1,p2)
        c = line.getCenter()
        radius = math.sqrt((abs(p1.getX()-p2.getX())**2)+(abs(p1.getY()-p2.getY())**2))/2
        

        e1 = c.clone()
        e1.move(-(0.5*(abs(p1.getX()-c.getX()))),-(0.5*(abs(p1.getX()-c.getX()))))
        e2 = e1.clone()
        e2.move((abs(p1.getX()-c.getX())),0)
        m = c.clone()
        m.move(0,0.75*radius)
        m1 = m.clone()
        m1.move(-(0.25*(abs(p1.getX()-c.getX()))),0)
        m2 = m1.clone()
        m2.move((0.5*(abs(p1.getX()-c.getX()))),0)
        
        head = drawFace(c,radius,win)
        
        eye1 = Circle(e1,radius*1/10)
        eye1.setFill("black")
        eye1.draw(win)

        eye2 = Circle(e2,radius*1/10)
        eye2.setFill("black")
        eye2.draw(win)

        nose = Circle(c,radius*1/5)
        nose.setFill("red")
        nose.draw(win)

        mouth = Line(m1,m2)
        mouth.setWidth(3)
        mouth.draw(win)

    win.getMouse()
    win.close()
    
main()
        
        
        

