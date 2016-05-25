#face.py
#this program draws a face
#by: Paul


from graphics import *

def main():
    win = GraphWin("face",400,400)
    head = Circle(Point(200,200),150)
    head.setFill("red")
    head.draw(win)

    eye1 = Circle(Point(130,130),25)
    eye1.setFill("white")
    eye1.draw(win)

    eye2 = Circle(Point(270,130),25)
    eye2.setFill("white")
    eye2.draw(win)

    pupil = Circle(Point(130,130),5)
    pupil.setFill("black")
    pupil.draw(win)
    pupil2 = Circle(Point(270,130),5)
    pupil2.setFill("black")
    pupil2.draw(win)
    

    nose = Polygon(Point(200,140), Point(180,220), Point(220,220))
    nose.setFill("brown")
    nose.draw(win)

    mouth = Oval(Point(130,250), Point(270,290))
    mouth.setFill("purple")
    mouth.draw(win)

    mostarch = Rectangle(Point(220,248),Point(180,230))
    mostarch.setFill("black")
    mostarch.draw(win)

    hat = Rectangle(Point(80,80),Point(320,90))
    hat.setFill("white")
    hat.draw(win)
    hat1 = Rectangle(Point(100,80),Point(300,10))
    hat1.setFill("black")
    hat1.draw(win)

    ear = Oval(Point(347,150),Point(380,218))
    ear.setFill("brown")
    ear.draw(win)
    ear1 = Oval(Point(20,150),Point(53,218))
    ear1.setFill("brown")
    ear1.draw(win)
    win.getMouse() # pause for click in window
    win.close()

main()
