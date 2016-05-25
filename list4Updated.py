#LList.py
#Linked list implementation of a subset of the Python List API
#by: Paul Chifita


class ListNode(object):
    """Internal helper class to represent node in a singly linked list.
    """

    def __init__(self, item = None, link = None):

        '''creates a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link'''

        self.item = item
        self.link = link


#----------------------------------------------------------------------

class LList(object):

    #------------------------------------------------------------

    def __init__(self, seq=()):

        """create an LList
        post: creates a list containing items in seq"""

        if seq == ():
            # No items to put in, create an empty list
            self.head = None
        else:
            # Create a node for the first item
            self.head = ListNode(seq[0], None)

            # Add remaining items keeping track of last node added
            last = self.head
            for item in seq[1:]:
                last.link = ListNode(item, None)
                last = last.link

        self.size = len(seq)


    #------------------------------------------------------------

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    #------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''

        if not(0 <= position < self.size):
            raise IndexError("index out of range: "+str(position))

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

    #------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list
        post: x is appended onto the end of the list'''

        # create a new node containing x
        newNode = ListNode(x)

        # link it into the end of the list
        if self.head is not None:
            # non-empty list
            node = self._find(self.size - 1)
            node.link = newNode
        else:
            # empty list
            # set self.head to new node
            self.head = newNode
        self.size += 1

    #------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item

    #------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

    #------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < len(self)
        post: the item at the specified position is removed from
        the list'''

        assert 0 <= position < self.size

        self._delete(position)

    #------------------------------------------------------------

    def _delete(self, position):

        #private method to delete item at location position from the list
        # pre: 0 <= position < self.size
        # post: the item at the specified position is removed from the list
        # and the item is returned (for use with pop)

        if position == 0:
            # save item from the initial node
            item = self.head.item

            # change self.head to point "over" the deleted node
            self.head = self.head.link

        else:
            # find the node immediately before the one to delete
            prev_node = self._find(position - 1)

            # save the item from node to delete
            item = prev_node.link.item

            # change predecessor to point "over" the deleted node
            prev_node.link = prev_node.link.link

        self.size -= 1
        return item

    #------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item

        pre: self.size > 0 and ((i is None or (0 <= i < self.size))

        post: if i is None, the last item in the list is removed
        and returned; otherwise the item at position i is removed
        and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        # default is to delete last item
        # i could be zero so need to compare to None
        if i is None:
            i = self.size - 1

        return self._delete(i)

    #------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and
              old elements from position i..oldsize-1 are at positions
              i+1..newsize-1'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)
        else:
            # find item that node is to be insert after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)
        self.size += 1

    #------------------------------------------------------------

    def __copy__(self):

        '''post: returns a new LList object that is a shallow copy of self'''

        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    #------------------------------------------------------------

    def __iter__(self):
        # iterator using Python generator (beautiful!)
        node = self.head
        while node is not None:
            yield node.item
            node = node.link

    #------------------------------------------------------------

    def getCursor(self):
        return LListCursor(self)

    #------------------------------------------------------------

    def __add__(self, lst2):
        """appends all the items of lst2 (a LList object) to end of the list

        post: returns a new LList object that has items from
                both lists concatenated"""

        new = LList()
        for i in self:
            new.append(i)
        for x in lst2:
            new.append(x)
        return new


class LListCursor(object):

    #------------------------------------------------------------

    def __init__(self, llist):
        self.lst = llist

        # create a dummy node at the front of the list
        self.header = ListNode("**DUMMY HEADER NODE**", llist.head)

        # point prev to just before the first actual ListNode
        self.prev = self.header

    #------------------------------------------------------------

    def done(self):

        """post: True if cursor has advanced past the last item
        of the sequence, false otherwise"""

        return self.prev.link is None

    #------------------------------------------------------------

    def getItem(self):

        """ pre: not self.done()
        post: Returns the item at the current cursor position"""

        return self.prev.link.item

    #------------------------------------------------------------

    def replaceItem(self, value):

        """ pre: not self.done()
           post: The current item in the sequence is value"""

        # exercise for reader
        self.prev.link.item = value
        #pass

    #------------------------------------------------------------

    def advance(self):

        """ post: cursor has advanced to the next position in the
        sequence. Advancing from the last item causes
        self.done() to be True"""

        self.prev = self.prev.link

    #------------------------------------------------------------

    def deleteItem(self):

        """ pre: not self.done()
        post: The item that cursor was pointing to is removed
        from the sequence and the cursor now points to
        the following item

        note: removing the last item in the sequence causes
        self.done() to be True"""

        self.prev.link = self.prev.link.link

        # first listnode _may_ have changed, update list head
        self.lst.head = self.header.link

    #------------------------------------------------------------
        
    def insertItem(self, value):
        """ post: value is added to the sequence at the position of
                  cursor.

            note: If self.done() holds before the call, value will be
                  added to the end of the sequence. In other cases,
                  the item that was at current position becomes the
                  next item."""
        
        current = self.prev.link
        new = ListNode(value, current)
        self.prev.link = new
        self.lst.head = self.header.link 

    
