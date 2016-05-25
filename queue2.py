#queue.py
#an implementation of a linked list Queue
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
        
class Queue(object):
    def __init__(self):
        self._front = None
        self._back = None
        self._count = 0

#----------------------------------------------------------------------
    def enqueue(self,item):
        #post: adds item at back of self

        newNode = ListNode(item)
        if self._back is not None:
            self._back.link = newNode
        else:
            self._front = newNode
        self._back = newNode
        self._count += 1        
#----------------------------------------------------------------------

    def front(self):
        #pre: self.size() > 0
        #post: returns item at front
        return self._front.item        
        
#----------------------------------------------------------------------
    def dequeue(self):
        #pre: self.size() > 0
        #post: returns and removes front item
        item = self._front.item
        self._front = self._front.link
        self._count -= 1
        if self._count == 0:
            self._back = None
        return item

#----------------------------------------------------------------------        
    def size(self):
        return self._count

#----------------------------------------------------------------------
    def isOrdered(self):
         #pre: items of each node of the queue are comparable
        #post: the queue is unchanged, and True is returned if the
        #objects in the queue are in order
        first = self._front
        last = self._front.link
        while last is not None:
            if first.item <= last.item:
                first = first.link
                last = last.link
            else:
                return False
        return True
        


