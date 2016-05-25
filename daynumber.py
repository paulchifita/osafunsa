#daynumber.py
#This program accepts a date as month/day/year, and then calculates the corresponding day number
#by: Paul Chifita

#This funtion check whether the year is Leap or not, and returns the results to be used later in the program
def isLeapYear(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

#The main defines the different variable to be used in the program, and also uses decisions to execute the different sequences of instructions for different cases
def main():
    print("\nThis program accepts a date as month/day/year, and then calculates\nthe corresponding day number")

    dateStr = input("\nEnter month,day and year numbers (month/day/year): ")

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    monthStr,dayStr,yearStr = dateStr.split("/")

    month,day,year = int(monthStr),int(dayStr),int(yearStr)
    
    monthStr = months[month - 1]

    date = monthStr + " " + str(day) + "," + str(year)
        
    dayNum = 31*(month - 1)+ day

    YearCondition = isLeapYear(year)
    
    print("\nThe year,",year,",is a Leap year: ",YearCondition)
    
    if YearCondition == True:
        if month > 2:
            dayNum = dayNum - (4*(month)+23)//10 + 1
            print("\nAs of the date, ",date,"the day number is ",dayNum)
        else:    
            dayNum = dayNum 
            print("\nAs of the date, ",date,"the day number is ",dayNum)
    elif YearCondition == False:
        if month > 2:
            dayNum = dayNum -(4*(month)+23)//10 
            print("\nAs of the date, ",date,"the day number is ",dayNum)
        else:
            dayNum = dayNum 
            print("\nAs of the date, ",date,"the day number is ",dayNum)
    else:
        if month <= 2:
            dayNum = dayNum
            print("\nAs of the date, ",date,"the day number is ",dayNum)
            
main()
