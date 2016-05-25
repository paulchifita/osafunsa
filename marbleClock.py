#marbleClock.py
#this program implements a simulation of a marble clock
#by: Paul Chifita

from queue2 import*
from Stack import*

class MarbleClock:
    def __init__(self,numMarbles):
        self.resv = Queue()
        self.oneMin = Stack()
        self.fiveMin = Stack()
        self.hour = Stack()

        assert numMarbles >= 27
        
        for i in range(numMarbles):
            self.resv.enqueue(i)

        
            
    def minute(self):
        m = self.resv.dequeue()
        self.oneMin.push(m)
        
        if self.oneMin.size() == 5:
            self.fiveMin.push(self.oneMin.pop())
            for i in range(4):
                d = self.oneMin.pop()
                self.resv.enqueue(d)
        if self.fiveMin.size() == 12:
            f = self.fiveMin.pop()
            self.hour.push(f)
            for i in range(11):
                h = self.fiveMin.pop()
                self.resv.enqueue(h)
        if self.hour.size() == 12:
            for i in range(12):
                hrs = self.hour.pop()
                self.resv.enqueue(hrs)
        self.cap = self.resv
                
    def run12hours(self):
        for i in range(720): #720 because there are 720 minutes in 12 hours
            self.minute()
                      
    def inOrder(self):
        if self.cap == self.resv:
            return True
        
            

    #----------------------------------------------------------------------
    def _getResv(self): #(Python) list of ints

        nums = []
        for i in range(self.resv.size()):
            nums.append(self.resv._front.item)
            self.resv.enqueue(self.resv.dequeue())
        return nums

def mClock():
    print("\nThis program implements a simulation of a Marble Clock.")
    print("It requires 27 or more marbles to run the clock")
    
    nMarbles = eval(input("\nEnter number of marbles (27 or more marbles): "))

    clock = MarbleClock(nMarbles)
    clock.run12hours()
    rounds = 1
    while clock.inOrder() != True:
        clock.run12hours()
        rounds += 1
        c = clock._getResv()
    print("\nWith "+str(nMarbles)+" marbles;")
    print("It took the marble clock, ",rounds," cycles, to get the marbles back in their original order")
    
if __name__ == "__main__": mClock()
