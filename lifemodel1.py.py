# lifemodel.py
#by paul chifita and Neal
#Model for Conway's Game of Life


class LifeCell:
    
    #A single cell in Conway's GOL A cell knows it's current value
    #(alive or not) and it's next value which is calculated from its
    #count of live neighbors. The cell changes to it's next state when
    #asked to update.

    def __init__(self):
        #Creates a new cell having current and next states of False
        
        self.alive = False
        self.next = False

    def setAlive(self, alive):
        #Directly sets the current liveness of this cell to the
        #value of alive (a Boolean).
    
        self.alive = alive

    def isAlive(self):
        #Returns a Boolean indicating whether this cell is currentlyalive.
        
        return self.alive
        

    def setNextState(self, neighborcount): 
        #Sets the next state of this cell based count of live neighbors
    
        if self.alive:
            if neighborcount == 2 or neighborcount == 3:
                self.next = True
            else:
                self.next = False
        else:
            if neighborcount == 3:
                self.next = True
            else:
                self.next = False

    def update(self):
        #Changes state of this cell to be the previously calculated
        #next state and return a Boolean indicating whether the new state
        #differs from the old
        
        oldState = self.alive
        self.alive = self.next
        
        return oldState != self.alive
                
 
class LifeModel:
    #A LiveModel is a grid of LifeCell that follows the rules of Conway's Game of Life.

    def __init__(self, rows, cols):#Done partially
        #Create a rowsXcols grid of LifeCell 
        
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.locations = [(r,c) for r in range(rows) for c in range(cols)]

        for c in range(self.cols):
            row = []
            for r in range(self.rows):
            
                cell = LifeCell()
                
                row.append(cell)
            self.cells.append(row)
            row = []
            

    def setAlive(self, row, col, alive):
        #Sets cell in location (row,col) to alive (a Boolean value)
        
        cell = self.cells[row][col]
        cell.setAlive(alive)

        

    def isAlive(self, row, col):
        #Returns whether the (row, col) is alive (Boolean)
        
        return self.cells[row][col].isAlive()

    def step(self):
        #Updates the grid to the next generation and return the list
        #of cell locations that changed state (e.g. [(3,4), (8,10)])
        

        for r,c in self.locations:
            cell = self.cells[r][c]
            cell.setNextState(self.countNeighbors(r,c))
            
        changed = []

        for r,c in self.locations:
            cell = self.cells[r][c]
            if cell.update():
                changed.append((r,c))
        return changed
        

    def countNeighbors(self, row, col):
        #Returns the number of (live neighbors) of cell in location (row,col)
        
        neighborcount = 0

        for i in range(row-1, row+2):

            for j in range(col-1, col+2):
                nr = i % self.rows
                nc = j % self.cols

                if (nr, nc) != (row,col) and self.isAlive(nr,nc):
                    neighborcount = neighborcount + 1
        return neighborcount
        
    
    def __str__(self):
        #Returns current state of model as a multi-line string.
        # - is used for dead cells and X for live cells.
        
        lines = []
        for row in self.cells:
            rowchars = []
            for cell in row:
                if cell.isAlive():
                    ch = "X"
                else:
                    ch = "-"
                rowchars.append(ch)
            lines.append("".join(rowchars))
        return "\n".join(lines)


    def loadString(self, s):
        #Sets the current state of according to contents of string s
        
        lines = s.split("\n")
        row = 0
        for line in lines:
            col = 0
            for ch in line:
                if ch == "X":
                    self.setAlive(row,col,True)
                elif ch == "-":
                    self.setAlive(row,col,False)
                
                    
                col = col + 1
            row = row + 1
        

def test():
    
    # The test function that creates a 20x20 model, loads the file
    #'test.txt' and runs 50 generations pausing between for the user
    #to press <Enter>.


    model = LifeModel(45,45)
    model.loadString(open("test2.txt").read())
    for i in range(50):
        print(model)
        input()        # pause for user to press <Enter>
        model.step()


if __name__ == "__main__":
    test()
