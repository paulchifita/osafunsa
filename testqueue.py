#testqueue.py
#by: Paul Chifita
import unittest
from queue2 import*

class TestQueue(unittest.TestCase):
    
    def testConstructor(self):
        q = Queue()
        self.assertEqual(q.size(),0)

    def testOneEnqueue(self):
        q = Queue()
        q.enqueue("one")
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.front(), "one")


unittest.main()
