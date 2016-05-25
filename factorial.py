#Facoral.py
#This program determines the value of the
#Paul Chifita


def main():
    n = eval(input("Enter the value of n: "))
    n2 = n
    lst= 1
    while n >= 1:
        lst = lst * n
        n = n - 1
    
    print("Factorial of ",n2," is: ",lst)

main() 
