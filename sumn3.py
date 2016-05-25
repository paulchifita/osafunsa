# sumn.py
# this program finds the sum of the cubes of the first n natural numbers.
# by paul

def main():
    print("This program finds the sum of the cubes of the first n natural numbers.")
    print()
    n = eval(input("Enter the nth term: "))
    print()
    sumn3 = ((n*(n+1))/2)**2
    print()
    print(sumn3)

main()
