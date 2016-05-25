#showhand.py
#A program that displays 5-card poker hands described in a file
#by: Paul Chifita

from graphics import*

def main():
    win = GraphWin("5-card poker hands", 700,500)
    win.setCoords(0,0,10,10)
    win.setBackground("yellow")
    
    message = Text(Point(5,9.5),"Enter the filename in the box below")
    message.setSize(15)
    message.setFill("black")
    message.setStyle("bold")
    message.draw(win)

    output = Entry(Point(5,8.9),20)
    output.draw(win)

    boxbut = Rectangle(Point(2.5,7.5),Point(7.5,8.5))
    boxbut.setFill("grey")
    boxbut.setOutline("black")
    boxbut.setWidth(5)
    boxbut.draw(win)
    button = Text(Point(5,8),"Click here to read file")
    button.setStyle("bold")
    button.setFill("red")
    button.setSize(12)
    button.draw(win)
    
    
    #wait for a mouse click
    win.getMouse()
    button.setText("Click for first set")
    message.setText("")

    
    #Get filename from user
    filename = output.getText()


    #Open and read the file
    infile = open(filename, 'r')
    output.undraw()
    
    
    #Read file from folder and print it out
    x = 4
    y = 5
    anchor = Point(x,y)

    for line in infile:
        hands = line.split()
        
        win.getMouse()   
        button.setText("Click two times to get next set")
        
        for card in hands:
            Image(Point(x,y), "cardset/" + card + ".gif").draw(win)
            x = x + 0.5
            y = y - 1
        x = 4
        y = 5
        
        
    #wait for mouse click to close window
    button.setText("Close window")
    message.setText("Click on button below to close window")
    win.getMouse() 
    win.close()

main()



    
            
