# distance.py

# This program determines the distance between two points it accepts.

# by: Paul Chifita



import math

def main():

	print("This program calculates the distance between two points it accepts.")
	print()
	print("Please enter the unit of measurement and the values of the cordinates for each point.")
	print("Point1: x1, y1")
	print("Point2: x2, y2")
	print()
	unit = input("unit: ")
	print()
	x1 = eval(input("x1: "))
	y1 = eval(input("y1: "))
	x2 = eval(input("x2: "))
	y2 = eval(input("y2: "))
	print()
	print("The measurement unit is: ",unit)
	print("Point1 has cordinates x1:",x1,"     " "y1:",y1, "respectively")
	print("Point2 has cordinates x2:",x2,"     " "y2:",y2, "respectively")
	print()
	x = (x2-x1)**2
	y = (y2-y1)**2
	distance = math.sqrt(x+y)
	print()
	print("The distance between point1 and point2 is ",round(distance,4), unit)


main()
