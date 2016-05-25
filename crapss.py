#craps.py
#this program simulates multiple games of craps and estimates the probability that the player wins.
#by: Paul Chifita and Kushboo Rana

from random import randrange


def main():
    intro = print("\nThis program simulates multiple games of craps and\nestimates the probability that the player wins.")
    n = inputs()
    wins = nGames(n)
    printSummary(n,wins)
    
def inputs():
    #returns one simulation parameter
    n =eval(input("\nEnter the number of games to sim: "))
    return n
    
def nGames(n):
    #Simulates n games of craps for a single player
    #Returns number of wins for the player
    wins=0
    
    for i in range(n):
        win = aGame()
        if win:
            wins = wins + 1
    return wins        
   
def aGame():
    #Simulates a single game for a player
    #Returns a Boolean to indicate whether or not the player needs to roll for point
    roll = rollDice()
    
    if roll == 7 or roll == 11:
        return True
    elif roll == 2 or roll == 3 or roll == 12:
        return False
    else:
        return rollForPoint(roll)
    


def rollForPoint(point2Mek):
    #point2Mek represents the roll the player needs to roll to win
    #returns a Boolean to indicate whether the player rolls for point or not
    roll = rollDice()
    while roll != point2Mek and roll != 7:
        roll = rollDice()
    return roll == point2Mek


def rollDice():
    #rolls the two dice and gives the sum of their outcomes
    sum = randrange(1,7)+randrange(1,7)
    return sum
    
def printSummary(n,wins):
    #prints the summary of probability that a player wins
    print("\nThe probability that a player wins is, ",round((wins/n),2),".")
    
if __name__ == '__main__': main()
