# Deck.py
# This program implements the Deck class with 52 cards in standard order
# by: Paul Chifita


from random import randrange
from Card3 import Card
  
class Deck(object):

    #------------------------------------------------------------

    def __init__(self,filename = None):

        """post: Creates a 52 card deck in standard order"""
        self.filename = filename
        cards = []
        if filename == None:
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    cards.append(Card(rank,suit))
            self.cards = cards
            
        else:
            infile = open(filename,"r")
            for line in infile:
                r,s = line.split()
                cards.append(Card(int(r),s))
            self.cards = cards
            infile.close()
        self.cards.reverse()
    #------------------------------------------------------------

    def size(self):
        """Cards left
        post: Returns the number of cards in self"""

        return len(self.cards)
    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card in self, and removes it from self.""" 
            
        if self.size() > 0:
            return self.cards.pop()
        else:
            return "There are no more cards left"

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck
        post: randomizes the order of cards in self"""


        n = self.size()
        cards = self.cards
        for i,card in enumerate(cards):
            pos = randrange(i,n)
            cards[i] = cards[pos]
            cards[pos] = card
            
