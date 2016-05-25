#chaos2.py
#This program computes a chaotic function and asks the user how many results to print
#by: Paul Chifita


def main():
    print("This program illustrates a chaotic funtion and asks the user how many results to print")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9*x*(1-x)
        print(x)
	
main()
