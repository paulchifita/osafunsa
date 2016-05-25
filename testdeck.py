# testdeck.py
# Unit test of Deck
# by: John Zelle 2/7/2013

import unittest
from newDeck3 import *

class TestDeck(unittest.TestCase):

    def testDefault(self):
        d = Deck()
        self.assertEqual(d.size(), 52)
        self.assertEqual(d.deal(), Card(2,'c'))
        self.assertEqual(d.size(), 51)
        self.assertEqual(d.deal(), Card(3,'c'))
        for i in range(11):
            d.deal()
        self.assertEqual(d.deal(), Card(2,'d'))
        for i in range(12):
            d.deal()
        self.assertEqual(d.deal(), Card(2,'h'))
        for i in range(12):
            d.deal()
        self.assertEqual(d.deal(), Card(2,'s'))
        for i in range(11):
            d.deal()
        self.assertEqual(d.deal(), Card(14,'s'))
        self.assertEqual(d.size(), 0)

    def testStacked(self):
        d = Deck("testdeck.txt")
        self.assertEqual(d.size(), 4)
        self.assertEqual(d.deal(), Card(2,'c'))
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.deal(), Card(3,'d'))
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.deal(), Card(4,'h'))
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.deal(), Card(5,'s'))

    def testShuffle(self):
        counts = [0]*4
        target = Card(4,'h')
        for i in range(10000):
            d = Deck("testdeck.txt")
            d.shuffle()
            for i in range(4):
                if d.deal() == target:
                    break
            counts[i] += 1
        for i,c in enumerate(counts):
            self.assertLess(abs(c-2500), 100, str(i)+" count is bad")
            

unittest.main()
        
