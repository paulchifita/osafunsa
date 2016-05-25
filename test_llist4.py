#test_llist4.py
#by: Paul Chifita (provided by Dr. Zelle)

import unittest

from list4Updated import *

class TestLList(unittest.TestCase):

    def setUp(self):
        self.lst1 = LList([1,2,3])
        self.lst2 = LList([4,5,6])

    def testAppend(self):
        self.lst1.append(4)
        self.assertEqual(list(self.lst1), [1,2,3,4])
        self.lst1.append("howdy")
        self.assertEqual(list(self.lst1), [1,2,3,4,"howdy"])

    def testAdd(self):
        result = self.lst1 + self.lst2
        self.assertIsInstance(result, LList)
        self.assertEqual(list(result), [1,2,3,4,5,6])
        self.assertEqual(list(self.lst1), [1,2,3])
        self.assertEqual(list(self.lst2), [4,5,6])

    def testCursorTraversal(self):
        c = self.lst1.getCursor()
        for i in range(1,4):
            self.assertFalse(c.done())
            self.assertEqual(c.getItem(), i)
            c.advance()
        self.assertTrue(c.done())

    def testCursorRemove(self):
        c = self.lst1.getCursor()
        c.deleteItem()
        self.assertEqual(list(self.lst1), [2,3])
        self.assertFalse(c.done())
        self.assertEqual(c.getItem(),2)
        c.advance()
        c.deleteItem()
        self.assertEqual(list(self.lst1), [2])
        self.assertTrue(c.done())

    def testReplaceItem(self):
        c = self.lst1.getCursor()
        c.replaceItem("hello")
        self.assertEqual(list(self.lst1),["hello",2,3])
        c.advance()
        c.replaceItem("linked")
        self.assertEqual(list(self.lst1),["hello","linked",3])
        c.advance()
        c.replaceItem("list")
        self.assertEqual(list(self.lst1),["hello","linked","list"])
        c.advance()
        self.assertTrue(c.done())

    def testInsertItem(self):
        c = self.lst1.getCursor()
        c.insertItem("hello")
        self.assertEqual(list(self.lst1),["hello",1,2,3])
        c.advance()
        c.advance()
        c.insertItem("linked")
        self.assertEqual(list(self.lst1),["hello",1,"linked",2,3])
        c.advance()
        c.advance()
        c.insertItem("list")
        self.assertEqual(list(self.lst1),["hello",1,"linked",2,"list",3])
        c.advance()
        c.advance()
        self.assertTrue(c.done())

unittest.main()
