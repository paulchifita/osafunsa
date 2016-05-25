#stats.py
#this program takes a set of exam scores as input and prints out a report that summerizes student performance.
#by: Paul Chifita

from math import sqrt

def get_scores():
    """Gets scores interactively from the user

    post: returns a list of numbers obtained from the user"""

    nums = []
    xStr = input("\nEnter a number: ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)

        xStr = input("\nEnter a number: ")
    return nums


def min_value(nums):
    """Finds the minimum among the numbers entered by the user

    pre: nums is a list of numbers and len(nums) > 0
    post: returns smallest number in nums"""

    min = nums[0] #first assumes the first number entered is the smallest
    for num in nums:
        if num < min: #checks if the numbers added to the are smaller than the 
            min = num #first entered and assigns the smallest later number as min
    return min


def max_value(nums):
    """Finds the maximum among the numbers entered by the user

    pre: nums is a list of numbers and len(nums) > 0
    post: returns largest number in nums"""

    max = nums[0] #first assumes the first number entered is the smallest
    for num in nums:
        if num > max: #checks if the numbers added to nums are larger than the 
            max = num #first entered and assigns the largest later number as max
    return max


def average(nums):
    """calculates the mean of the numbers entered by the user

    pre: nums is a list of numbers and len(nums) > 0
    post: returns the mean (a float) of the values in nums"""

    sum = 0.0 #initializes the sum of all numbers in nums
    for num in nums: #looks up all the numbers in nums and then,
        sum += num #finds the sum
    return (sum/(len(nums)))


def std_Dev(nums):
    """calculates the standard deviation of the numbers entered by user

    pre: nums is a list of numbers and len(nums) > 1
    post: returns the standard deviation (a float) of the value in nums"""

    xbar = average(nums)
    sum = 0.0
    for num in nums:
        sum += (xbar - num)**2
    return sqrt(sum/(len(nums) - 1))


def main():
    print("This program takes a set of exam scores from a user as input and prints out a\nreport that summerizes student performance.")
    print("\n \nPLEASE READ THE INSTRUCTIONS BELOW!\n \nAfter entering a number:\n1. Press enter once to get next value\n2. Press Enter twice to print the report")
    scores = get_scores()

    print("\nThe minimum exam score is: "+str(round((min_value(scores)),2))+"%\nThe maximum exam score is: "+str(round((max_value(scores)),2))+"%\nThe average exam score is: "+str(round((average(scores)),2))+"%\nThe standard deviation of the exam scores is: "+str(round((std_Dev(scores)),2))+"\n \nAbove is the summarized report of the values you entered")  

main()
    
    
    
