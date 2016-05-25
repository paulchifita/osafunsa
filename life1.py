# life.py
#by: Paul Chifita and Neal
#A model of Conway's game of life


import time
from tkinter.filedialog import asksaveasfilename, askopenfilename

from graphics import *
from checkbox import CheckBox
from button import Button
from gridview1 import GridView 
from lifemodel import LifeModel

class LifeApp:

    def __init__(self,win):
        self.win = win
        self.drawGUI(win)
        self.locations = [(r,c) for r in range(45) for c in range(45)]
        self.model = LifeModel(45,45)
        self.animating = False         # the model/display is not changing
        self.running = True            # the application is running


    def drawGUI(self, win):
        # draws gui components including: grid, runbutton, pausebutton, stepbutton
        # savebutton, loadbutton, clearbutton, quitbutton
        
        self.grid = GridView(win,Point(50,60), 2.1,45,45)
        self.runbutton = Button(win,Point(12.5,98),6,3,"Run")
        self.runbutton.activate()
        self.pausebutton = Button(win,Point(25,98),8.5,3,"Pause")
        self.pausebutton.activate()
        self.stepbutton = Button(win,Point(37.5,98),7,3,"Step")
        self.stepbutton.activate()
        self.savebutton = Button(win,Point(62.5,98),7,3,"Save")
        self.savebutton.activate()
        self.loadbutton = Button(win,Point(75,98),7,3,"Load")
        self.loadbutton.activate()
        self.clearbutton = Button(win,Point(50,98),7.5,3,"Clear")
        self.clearbutton.activate()
        self.quitbutton = Button(win,Point(87.5,98),6,3,"Quit")
        self.quitbutton.activate()

    def run(self,win):
        #defines the event loop
        
        while self.running:
            self.setButtonState()
            pt = self.win.checkMouse()
            if pt != None:
                self.handleEvent(pt)
            if self.animating:
                changes = self.model.step()
                self.updateView(changes)
            time.sleep(.1)
        self.win.close()


    def setButtonState(self):
        # sets proper activation of run and pause buttons
        
        if self.animating == True:
            self.runbutton.deactivate()
            self.pausebutton.activate()
        else:
            self.runbutton.activate()
            self.pausebutton.deactivate()
        


    def updateView(self,locations):
        # Sets checkboxes in locations of grid to reflect their state
        # in the life model. Locations is a list of (row,column) pairs.
        
        for r,c in self.locations:
            value = self.model.isAlive(r,c)
            self.grid.setChecked(r,c,value)
        self.win.update()
            


    def handleEvent(self, pt):
        # The user clicks at point pt, take appropriate action
        
        if self.quitbutton.clicked(pt):
            self.running = False
        elif self.runbutton.clicked(pt):
            self.animating = True
        elif self.pausebutton.clicked(pt):
            self.animating = False

        if self.grid.clicked(pt):
            self.on_grid()            
        elif self.stepbutton.clicked(pt):
            self.on_step()
        elif self.loadbutton.clicked(pt):
            self.on_load()
        elif self.savebutton.clicked(pt):
            self.on_save()
        elif self.clearbutton.clicked(pt):
            self.on_clear()
            
            


    def on_step(self):
        # turns off animation 
        # call step on your life model to get a list of changed locations
        # call your LifeApps updateView passing the list of changed locations
       
        self.animating = False
        
        x = self.model.step()
        self.updateView(x)
       
                
    def on_load(self):
        #loads a file and displays its saved string as checkboxes on the gridview
        
        self.animating = False
        fromFile=askopenfilename()
        self.model.loadString(open(fromFile).read())
        self.updateView(self.locations)

    def on_save(self):
        #saves the current checkboxes drawn on the grid view as string to a specified file
        
        self.animating = False
        
        outFile=asksaveasfilename()
        f=open(outFile, 'w')
        f.write(str(self.model))
        

    def on_grid(self):
        #allows the user to click on the grid
        
        i,j = self.grid.getLocation()
        oldValue = self.model.isAlive(i,j)
        self.model.setAlive(i,j, not oldValue)
        self.updateView([(i,j)])
                  

    def on_clear(self):
        #clears the grid to update it to its original state
        
        for r in range(45):
            for c in range(45):
                
                self.model.setAlive(r,c,False)
        self.updateView(self.locations)

            
def main():
    # runs the Life application
    
    win = GraphWin("Game of Life", 650, 650, autoflush=False)
    win.setCoords(0,100,100,0)
    app = LifeApp(win)
    app.run(win)
   
    
if __name__ == "__main__": main()
    
    

    


                
        
