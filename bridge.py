# mybridge.py
# This program implements the Bridge Game
# by: Paul Chifita and Neal Bazirake, Jan-2013


from Card3 import*
from newDeck3 import*
from mybridgehand import*


def bridge():
    ####print intro from words below
    print("\n           Welcome to the BRIDGE GAME. Enjoy!!!\n \n")
    print("\nThis program simulates the dealing of four thirteen-card hands from") 
    print("a shuffled deck. The program then determines how many points each of the")
    print("four hands is worth based on the following criteria:")
    print("\n     -Each Ace is worth 4 points.")
    print("     -Each King is worth 3 points.")
    print("     -Each Queen is worth 2 points.")
    print("     -Each Jack is worth 1 point.")
    print("     -A doubleton suit (exactly two cards in that suit) is worth 1 points.")
    print("     -A Singleton suit (exactly one card in that suit) is worth 2 points.")
    print("     -A void suit (no cards in the suit) is worth 3 points.")
    print("\nThe program deals 4 hands and neatly display them along with the associated")
    print("point totals. The four hands are customarily labeled 'North', 'East', 'South'")
    print("and 'West'.\n \nThe program also prints out whether each hand has an 'opening bid.'")
    print("A hand opens if it meets the following two conditions:")
    print("\n     -The hand must have at least 13 points.")
    print("     -The hand must have either:")
    print("         * A suit with at least 5 cards.")
    print("         * A suit with 4 cards including at least one honor")
    print("           (Ace, King, Queen, or Jack).")


    while True:
        print("\n================================================================================")
        print("\nDo you want to use a random deck or one constructed from a file, ")
        print("or quit?")
        print("\n     1. Use a random deck")
        print("     2. Read from file")
        print("     3. Quit")
        
        ans = input("\nChoose your option (random, file or quit) and <Enter>?: ")

        if ans == "quit":
            print("\n*******************************[YOU QUIT]**************************************")
            break
        elif ans == "file":
            fname = input("\nEnter the file name (e.g. deck.txt) and <Enter>: ")
            d = Deck(fname)
            d.shuffle()     
        elif ans == "random":
            d = Deck()
            d.shuffle()
        else:
            print("\n*********************Ooops, you did not choose any OPTION**********************")
            break
        
        handsStr = "North East South West"

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
        
        for h in hands:
            h.sort()
            h.dump()
            for suit in Card.SUITS:
                suit = s
            if (h.handPoints() >= 13 and
                (h.countSuit(suit) >= 5 or h.hasHonor() is True)):
                print(h.label+" hand has "+str(h.handPoints())+" points, and is bidable\n")
            else:
                print(h.label+" hand has "+str(h.handPoints())+" points, and unbidable\n")

if __name__ == "__main__":
    bridge()
