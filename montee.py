#monte.py
#this program creates a Three-Button Monte game using CheckBox and Button
#by: Paul Chifita

from graphics import *
from button import Button
from checkbox import CheckBox
from random import randrange


def drawBoxes(win):
    
    #this function creates three checkboxes drawn labeled as
    #Box 1, Box 2, and Box 3, and returns the three boxes.
    b1 = CheckBox(win, Point(2,5),2)
    b2 = CheckBox(win, Point(4.5,5),2)
    b3 = CheckBox(win, Point(7,5),2)
    
    b1Txt = Text(Point(2,3),"Box 1")
    b1Txt.draw(win)
    b2Txt = Text(Point(4.5,3),"Box 2")
    b2Txt.draw(win)
    b3Txt = Text(Point(7,3),"Box 3")
    b3Txt.draw(win)

    return b1, b2, b3

def userBoxInteraction(win, b1, b2, b3, done):
    
    #this function allows the user to click in the window and
    #enforces the following rules:      
    #1) a click inside b1, b2, or b3 causes it to become the selected
    #(checked) box, while the other two are unselected.            
    #2)a click inside done (the "Done" button) terminates interaction
    #3)a click anywhere else is ignored.                                 
    p = win.getMouse()
    while not done.clicked(p):
        if b1.clicked(p):
            b1.setChecked(True)
            b2.setChecked(False)
            b3.setChecked(False)
        elif b2.clicked(p):
            b2.setChecked(True)
            b1.setChecked(False)
            b3.setChecked(False)
        elif b3.clicked(p):
            b3.setChecked(True)
            b2.setChecked(False)
            b1.setChecked(False)
        
        p = win.getMouse()
        
    
def determineResult(b1, b2, b3):
    
    #this function picks a random number (1-3) and determines
    #whether the corresponding box is checked.      
    # it also returns a string message indicating which one was the
    #"correct" box and whether the user wins or loses.                           
    num = randrange(1,4)
    box = [b1, b2, b3]
    
    if box[0].isChecked():
        if num == 1:
            return "The winning box was number " + str(num)+"\nYou WIN!"
        else:
            return "The winning box was number " + str(num)+"\nYou LOSE!"
    elif box[1].isChecked():
        if num == 2:
            return "The winning box was number " + str(num)+"\nYou WIN!"
        else:
            return "The winning box was number " + str(num)+"\nYou LOSE!"
    elif box[2].isChecked():
        if num == 3:
            return "The winning box was number " + str(num)+"\nYou WIN!"
        else:
            return "The winning box was number " + str(num)+"\nYou LOSE!"

 

def main():
    
    #the main creates a window with useful coordinates and also         
    #create a text object for displaying initial instructions
    #to pick a box
    #it creates and draw the three boxes and also creates the Done button                                   (done)
    #it interactively allows the user to choose a box, determine the final
    #result and display that result.                                       
    win = GraphWin("Three Button Monte",250,250)
    win.setBackground("magenta")
    win.setCoords(0,0,9,9)
    mssg = Text(Point(4.5,8),"Choose a box and click Done")
    mssg.setStyle("bold italic")
    mssg.draw(win)
    by = Text(Point(2,.3),"written by paul b. c\n11/28/12:400AM")
    by.setStyle("italic")
    by.setSize(7)
    by.draw(win)
    
    
    b1,b2,b3 = drawBoxes(win)
    
    done = Button(win,Point(4.5,1.5),2,1,"Done")
    done.activate()

    userBoxInteraction(win, b1, b2, b3, done)

    result = determineResult(b1, b2, b3)
    
    mssg.setText(result)

    #wait for mouse click to terminate 
    win.getMouse()
    win.close()
    
if __name__ == "__main__":main()
