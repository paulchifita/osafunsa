# mybridgehand.py
# this program implements a labeled collection of cards than can be sorted
# by: Paul Chifita and Neal Bazirake, Jan-2013

from Card3 import*

class Hand(object):
    """A labeled collection of cards that can be sorted"""

    #------------------------------------------------------------

    def __init__(self, label=""):
        """Create an empty collection with the given label."""

        self.label = label
        self.cards = []

    #------------------------------------------------------------

    def add(self, card):
        """adds a card to the hand"""

        self.cards.append(card)

    #------------------------------------------------------------

    def sort(self):
        """ arranges the cards in descending bridge order."""
        cards0 = self.cards
        cards1 =[]
        while cards0 != []:
            next_card = max(cards0)
            cards0.remove(next_card)
            cards1.append(next_card)
        self.cards = cards1
   
    #------------------------------------------------------------

    def dump(self):
        """prints out contents of the hand"""

        print("\n"+self.label + "'s Cards:")
        for c in self.cards:
            print("   ", c)
            
    #------------------------------------------------------------

    def countRank(self,r):
        """post: returns number of cards of rank r in hand"""

        count = 0
        for c in self.cards:
            if c.rank() == r:
                count += 1
        return count

    #------------------------------------------------------------

    def countSuit(self,s):
        """post: returns number of cards of suit s in hand"""

        count = 0
        for c in self.cards:
            if c.suit() == s:
                    count += 1
        return count

    #------------------------------------------------------------

    def hasHonor(self):
        """post: returns True iff hand has an honor in suits"""

        return self.countRank(14) > 0 or self.countRank(13) > 0 or self.countRank(12) > 0 or self.countRank(11) > 0

    #------------------------------------------------------------
    
    def ranksValue(self):
        """post: returns, in terms of ranks, the points each card in hand is worth"""
        total = 0
        
        for c in self.cards:
            if c.rank() == 14:
                total += 4 * self.countRank(14)
            elif c.rank() == 13:
                total += 3 * self.countRank(13)
            elif c.rank() == 12:
                total += 2 * self.countRank(12)
            elif c.rank() == 11:
                total += 1 * self.countRank(11)
        return total

    #------------------------------------------------------------
    
    def suitsValue(self):
        """post: returns, in terms of ranks, the points each card in hand is worth"""
        
        total = 0
        for c in self.cards:
            if self.countSuit(c.suit()) == 2:
                total += 1
            elif self.countSuit(c.suit()) == 1:
                total += 2
            elif self.countSuit(c.suit()) == 0:
                total += 3
        return total

    #------------------------------------------------------------
    
    def handPoints(self):
        """post: returns points each hand is worth"""
        
        return self.ranksValue() + self.suitsValue()
        
    #------------------------------------------------------------
