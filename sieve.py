#sieve.py
#This program implements the sieve of Eratosthenes, a famous
#algorithm for finding all the prime the numbers up to a certain value
#by: Paul Chifita

import copy
from list4Updated import*

def primesList():
    
    print("\nThis program implements the sieve of Eratosthenes,")
    print("a famous algorithm for finding all the prime the")
    print("numbers up to a certain (number input by the user) value")
    
    
    #place the numbers 2 through n in a list
    n = eval(input("\nEnter a number: "))
    primeList = LList(range(2,n + 1,1))

    #start primecursor at the front of the list ??????
    primecursor = primeList.getCursor()

    while not primecursor.done():

        #prime = value at primecursor
        prime = primecursor.getItem()
        
        #create checkcursor as a copy of primecursor
        checkcursor = copy.copy(primecursor)
        
        #advance checkcursor
        checkcursor.advance()

        while not checkcursor.done():
            item = checkcursor.getItem()

            if item % prime == 0:

                checkcursor.deleteItem()           

            else:

                checkcursor.advance()

        primecursor.advance()

    print("\nBelow are all the prime numbers up to "
          +str(n)+"\n",list(primeList))


if __name__ == "__main__": primesList()

    
        
