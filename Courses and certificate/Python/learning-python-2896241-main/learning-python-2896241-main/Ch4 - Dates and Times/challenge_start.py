# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# a function that counts the number of weekdays within a given month


def countdays(pYear, pMonth, pDay):
    daycount = 0
    weekList = calendar.monthcalendar(pYear, pMonth)
    # print(weekList)
    # week variable contain all days within a week while the weeklist contain all the week within a month
    for week in weekList:
        if week[pDay] != 0:
            daycount += 1
    return daycount


print("Day counter program \n")
run = True

while run:
    try:
        print("Which day do you want to count")
        print("0- For Monday")
        print("1- For Tuesday")
        print("2- For Wednesday")
        print("3- For Thursday")
        print("4- For Friday")
        print("5- For Saturday")
        print("6- For Sunday")
        print("Exit- To close the program")

        day = input("? ")
        if day == "Exit":
            run = False
            break
        theday = int(day)

        year = input("Enter the year ")
        theyear = int(year)

        month = input("Enter the month ")
        themonth = int(month)
        result = countdays(theyear, themonth, theday)
        print("There are " + str(result) + " within that specific month and year")
        print("-------------------------\n")
    except Exception as e:
        print(e)
        print("Sorry, that's not valid input")
# countdays(2023, 1, 1)
