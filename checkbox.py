#checkbox.py
#this program creates a simple widget for displaying a square cell that is either "checked" or "unchecked.
#by: Paul Chifita

from graphics import*


class CheckBox:

    def __init__(self,win,center,size):

        #computes the values for the dimensions of the checkbox
        Len = size/2.0
        x,y = center.getX(),center.getY()
        self.xmax,self.ymax = x + Len, y + Len
        self.xmin,self.ymin = x - Len, y - Len

        #p1, p2 create the opposite vertices of the checkbox
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)

        #draw the checkbox
        self.box = Rectangle(p1,p2)
        self.box.setFill("grey")
        self.box.draw(win)

        #set the initial state of the checkbox to "unchecked"
        self.checked = False
        self.setChecked(self.checked)
         
        
    def setChecked(self,checked):
        
        #set the status of the checkbox to checked (a Boolean) value
        self.checked = checked

        #if checked is True, the checkbox appears selceted, or else if False,
        #it appears unselected
        if checked == True:
            self.box.setFill("black")
            self.box.setWidth(2)
            self.box.setOutline("white")
        elif checked == False:
            self.box.setFill("grey")
            self.box.setWidth(1)
            self.box.setOutline("black")
            


    def isChecked(self):

        #returns a Boolean indicating whether the checkbox is selected
        return self.checked
    
    def clicked(self,p):

        #returns True if Point p lies inside the checkbox
        return(self.clicked and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
        

def test():

    #creates a window containing a checkbox and handles 10 mouse clicks.
    #clicking in the checkbox toggles it between checked and unchecked.
    win = GraphWin("Test CheckBox")
    win.setCoords(-5,-5,5,5)
    cb = CheckBox(win, Point(0,0), 1)
    
    for i in range(10):
        pt = win.getMouse()
        if cb.clicked(pt):
            currState = cb.isChecked()
            cb.setChecked(not currState)
    win.close()
    

if __name__ == "__main__": test()
