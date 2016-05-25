#BridgeGui.py
#This program implements the Bridge game
#By: Neal Bazirake and Paul Chifita

from graphics import *
from button import Button
from Card3 import*
from newDeck3 import*
from mybridgehand2 import*


def showhand(h,ypos,win):

    cards = h.getCards()
    x = 150    
    for card in cards:
        filename = card.suit() + str(card.rank())
        Image(Point(x,ypos), "cardset/" + filename + ".gif").draw(win)
        x = x + 20
            
def weSeeCards():
    win = GraphWin("Bridge Hand",900,600)
    win.setBackground("gold")
    
    mess = Text(Point(445,70),"Welcome to the Bridge game. This game deals 4 hands and, neatly displays them along with\nthe associated point totals and indicates whether the hand is or not biddable."
                "The dealing of\nhands is done either at random or from a deck supplied as an input file. So you need to choose\nwhether to use a random deck or one constructed from a file. For a random deck, click on\nthe 'Random deck button', to construct from a file, click on the 'From file button'\nand to terminate the game click on the 'Quit button'.")
    mess.setTextColor("blue")
    mess.setFace("helvetica")
    mess.setSize(12)
    mess.setStyle("bold italic")
    
    mess.draw(win)

    quitbutton = Button(win,Point(750,170),55,20,"Quit")
    quitbutton.activate()
    fromfilebutton = Button(win,Point(300,170),85,20,"From file")
    fromfilebutton.activate()
    randomdeckbutton = Button(win,Point(150,170),115,20,"Random deck")
    randomdeckbutton.activate()
    runbutton = Button(win,Point(450,170),50,20,"Run")
    runbutton.activate()
    
    pt = win.getMouse()
    
    while True:
        
        if quitbutton.clicked(pt):
            win.close()
        
        elif fromfilebutton.clicked(pt):
            randomdeckbutton.deactivate()
            mess.setText("Enter the file name you want to construct the deck from (in the entry box below the 'From file button'),\nand click on the 'Run button' to print out the hands, their associated point totals and bidding status of each hand.\nClick on the 'Quit button' to terminate game.")
            output = Entry(Point(300,200),10)
            output.setFill("grey")
            output.draw(win)
            
            win.getMouse()
            filename = output.getText()
            if runbutton.clicked(pt):
                output.undraw()
            d = Deck(filename)
            d.shuffle()
            output.undraw()
            runbutton.deactivate()
            fromfilebutton.deactivate()
            
                
                
        elif randomdeckbutton.clicked(pt):
            fromfilebutton.deactivate()
            runbutton.deactivate()
            d = Deck()
            d.shuffle()
            
        handsStr = "\nNorth \nEast \nSouth \nWest"
        '''\nNorth \nEast \nSouth \nWest'''

        n,e,s,w = handsStr.split()
        n = Hand(n)
        e = Hand(e)
        s = Hand(s)
        w = Hand(w)
        
        for i in range(13):
            n.add(d.deal())
            e.add(d.deal())                
            s.add(d.deal())
            w.add(d.deal())
        
        hands = [n,e,s,w]
        mess.setText("Below are the hands you created along with their associated point totals,\nand the statements of whether a hand has an 'opening bid'\nClick on the 'Quit button' to terminate game.")
        
        y = 250
        
        for h in hands:
            h.sort()
            h.dump()
            showhand(h,y,win)
            for st in Card.SUITS:
                if (h.handPoints() >= 13 and
                    (h.countSuit(st) >= 5 or
                     (h.countSuit(st) == 4 and h.hasHonor(st)))):
                    Text(Point(600,y),h.label+" hand has "+str(h.handPoints())+" points, and is biddable").draw(win)
                    break
            else:
                Text(Point(600,y),h.label+" hand has "+str(h.handPoints())+" points, and is unbiddable").draw(win)
            y += 100    
           
        win.getMouse()
        win.close()
        
if __name__ == "__main__":
    weSeeCards()
    
