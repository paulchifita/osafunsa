#lighteninggui.py
#This program displays a gui that calculates the distance of the lightening strike
#by: Paul and Abdo


from graphics import *

def main():
    win = GraphWin("Distance to lightening strike calculator", 400, 300)
    win.setCoords(0.0,0.0,3.0,4.0)

    # Draw the interfacce
    Text(Point(1,3), " Time:").draw(win)
    Text(Point(1,1), "Distance is:").draw(win)
    input = Entry(Point(2,3),5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Calculate")
    button.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)

    #wait for a mouse click
    win.getMouse()

    #convert input
    seconds = eval(input.getText())
    time = seconds
    speed = 1100
    distance = (speed)*(time)

    #display output and change button
    output.setText(distance)
    button.setText("Quit")

    #wait for click and then quit
    win.getMouse()
    win.close()


main()

