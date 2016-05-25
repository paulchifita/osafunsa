# gridview.py
#by paul chifita and Neal
#A gridview is a rectangular array of checkboxes. Specific boxes are accessed by their row and column number (numbering starts at 0).

from graphics import *
from checkbox import CheckBox

class GridView:

    def __init__(self, win, center, boxSize, rows, cols):
        """Create a GridView in win having the given center point,
        checkbox size, with the specified number of rows and columns.
        """
        self.win = win
        self.boxSize = boxSize
        self.cols = cols
        self.rows = rows

        bcentre = center.clone()
        bcentre.move(-(center.getX()-boxSize)+boxSize, -(center.getY()-boxSize*.8))

        self.boxes = []
       
        #build a row of checkboxes and append  
        #it to boxes 
         
        for c in range(self.cols):
            row = []
            for r in range(self.rows):
            #build a row of checkbox add to rows
                cb = CheckBox(win, bcentre, boxSize)
                bcentre.move(boxSize,0)
                row.append(cb)
            self.boxes.append(row)
            row = []
            bcentre.move(-cols*boxSize, boxSize)

        self.value = False

        
    def setChecked(self, row, col, value):
        """Set the checkbox as position (row,col) according to value
        True is checked, False is unchecked.
        """
        cb = self.boxes[row][col]
        cb.setChecked(value)

    def isChecked(self, row, col):
        """Return a Boolean indicating whether the checkbox in location
        (row, col) is currently checked or not.
        """
        return self.boxes[row][col].isChecked()
            

    def clicked(self, pt):
        """Return a Boolean indicating if point pt is anywhere inside the grid
        As a side-effect, it stores the (row, col) location of which cell was
        clicked for later retrieval via getLocation.
        """
        for r in range(self.rows):
            for c in range(self.cols):
                cb = self.boxes[r][c]
                if cb.clicked(pt):
                    self.locationClicked = (r,c)
                    return True
        return False

    def getLocation(self):
        """Return the (row,col) location of the box that was found in the
        latest call to clicked(pt).
        """
        return self.locationClicked
      
               
               
            
    
def test():
    """A small GridView that allows user to 'draw' a picture by clicking
    boxes on and off. 
    """
    win = GraphWin("GridTest", 500, 500,autoflush=True)
    win.setCoords(0,100, 100, 0)
    gv = GridView(win, Point(50,50), 4.35 , 20, 20)
    while True:
        pt = win.getMouse()
        if gv.clicked(pt):
            i,j = gv.getLocation()
            oldValue = gv.isChecked(i,j)
            gv.setChecked(i,j, not oldValue)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test()

        
