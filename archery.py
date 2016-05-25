#archery.py
#This program draws an archery target and allows the user to click five times to represent arrows shot at the target
#by: Paul Chifita

from math import*
from graphics import*

#This function uses the circle object to draw the archery target
def drawTarget(win):
    radius = 5

    for color in [("white"),("black"),("blue"),("red"),("yellow")]:
        ring = Circle(Point(0,0),radius)
        ring.setFill(color)
        ring.draw(win)
        radius = radius = radius - 1


#This function sets the decision to excute different sequences of instructions
def getScore(dist):
    if dist <= 1:
        return 9
    elif dist <= 2:
        return 7
    elif dist <= 3:
        return 5
    elif dist <= 4:
        return 3
    elif dist <= 5:
        return 1
    else:
        return 0

    
#This function draws circles at points the user clicks on the target to represent arrows
def drawShot(shot,win):
    Shot = Circle(shot,0.25)
    Shot.setFill("black")
    Shot.setOutline("white")
    Shot.setWidth(2)
    Shot.draw(win)

    
#This function defines the various formulas used in the progrom, and the user input, which is will be the mouse clicks
def playGame(win,mssg):
    ShotScore = Text(Point(-5.5,-9),"Shot score: 0")
    ShotScore.setSize(14)
    ShotScore.setStyle("bold italic")
    ShotScore.setTextColor("blue")
    ShotScore.draw(win)

    Score = Text(Point(5,-9),"Your current score is: 0")
    Score.setSize(14)
    Score.setStyle("bold italic")
    Score.setTextColor("blue")
    Score.draw(win)

    win.getMouse()

    score = 0

    for shots in [("First"),("Second"),("Third"),("Fouth"),("Last")]:
        mssg.setText("Take your " + shots + " shot")
        shot = win.getMouse()
        dist = sqrt((shot.getX()**2) + (shot.getY()**2))

        drawShot(shot,win)
        
        onShot = getScore(dist)
        score = onShot + score

        ShotScore.setText(shots + " shot score is: " + str(onShot))
        Score.setText("Cumulative score is: " + str(score))

    tScore = Text(Point(0,0),"YOUR TOTAL SCORE IS: " + str(score))
    tScore.setSize(30)
    tScore.setFace("helvetica")
    tScore.setStyle("bold italic")
    tScore.setTextColor("magenta")
    tScore.draw(win)

    mssg.setText("GAME OVER!!!\nClick on the archery target to end game")
    
        
#The calls the functions defined above to make the program run
def main():
    win = GraphWin("Playing Archery",600,600)
    win.setCoords(-10,-10,10,10)
    win.setBackground("cyan")

    drawTarget(win)
    
    mssg = Text(Point(0,8),"You only have five shots to play, so do your best.\nClick on the archery target to start playing")
    mssg.setSize(14)
    mssg.setStyle("bold italic")
    mssg.setTextColor("black")
    mssg.draw(win)
    
    playGame(win,mssg)

    win.getMouse()
    win.close()

main()

    

    
        
        

    


