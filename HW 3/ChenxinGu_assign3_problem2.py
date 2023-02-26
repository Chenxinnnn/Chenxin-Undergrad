#Chenxin Gu, Oct 4nd, Section 3, ChenxinGu_assign3_problem2.py
date = int(input("Enter a date (YYYYMMDD): "))

#Because the year is the first 4 digits of the number, we can get it by dividing by 10000 and take the integer part.
#recognize the month and day as we do in the former assignment by using division and module.
year = int(date / 10000)
date_divided_by_100 = date / 100
month = int(date_divided_by_100) % 100
day = date % 100

#First examine if the number year is a leap year.
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")

    #If the year is a leap year, then 29 will be also valid for a date in February.
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: 
        if 1 <= day <= 31:
            #We have already checked that the date is valid, now we just need to rename the months and dates.
            #rename the months.
            if month == 1:
                month_printed = "January"
            if month == 3:
                month_printed = "March"
            if month == 5:
                month_printed = "May"
            if month == 7:
                month_printed = "July"
            if month == 8:
                month_printed = "August"
            if month == 10:
                month_printed = "October"
            if month == 12:
                month_printed = "December"
            #Now rename the dates. 
            if day == 1 or day == 21 or day == 31:
                day_printed = str(day) + "st"
            if day == 2 or day == 22:
                day_printed = str(day) + "nd"
            if day == 3 or day == 23:
                day_printed = str(day) + "rd"
            elif day != 1 and day != 2 and day != 3 and day != 21 and day != 22 and day != 23 and day != 31:
                day_printed = str(day) + "th"
            #Now print out the results
            print(month_printed, day_printed, "is a valid date in", year)
        #If the user gives an invalid date, then tell them it is invalid.  
        else:
            print("This is not a valid date in", year)
            
    #Discuss the months with 30 dates with basically the same logic as before.
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            if month == 4:
                month_printed = "April"
            if month == 6:
                month_printed = "June"
            if month == 9:
                month_printed = "September"
            if month == 11:
                month_printed = "November"

            if day == 1 or day == 21:
                day_printed = str(day) + "st"
            if day == 2 or day == 22:
                day_printed = str(day) + "nd"
            if day == 3 or day == 23:
                day_printed = str(day) + "rd"
            elif day != 1 and day != 2 and day != 3 and day != 21 and day != 22 and day != 23:
                day_printed = str(day) + "th"
                
            print(month_printed, day_printed, "is a valid date in", year)
        else:
            print("This is not a valid date in", year)
            
    #Finally discuss February. Because we are now discussing leap years, 29 is a valid date.
    elif month == 2:
        if 1 <= day <= 29:
            month_printed = "February"
            if day == 1 or day == 21:
                day_printed = str(day) + "st"
            if day == 2 or day == 22:
                day_printed = str(day) + "nd"
            if day == 3 or day == 23:
                day_printed = str(day) + "rd"
            elif day != 1 and day != 2 and day != 3 and day != 21 and day != 22 and day != 23:
                day_printed = str(day) + "th"
            print(month_printed, day_printed, "is a valid date in", year)
        else:
            print("This is not a valid date in", year)
    #If the user gives a month other than 1-12, then tell them it is invalid.        
    else:
        print("This is not a valid date in", year)

#Then, discuss the other years. Basically the same logic with 29 not a valid date for February.   
else:
    print(year, "is NOT a leap year")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: 
        if 1 <= day <= 31:
            if month == 1:
                month_printed = "January"
            if month == 3:
                month_printed = "March"
            if month == 5:
                month_printed = "May"
            if month == 7:
                month_printed = "July"
            if month == 8:
                month_printed = "August"
            if month == 10:
                month_printed = "October"
            if month == 12:
                month_printed = "December"

            if day == 1 or day == 21 or day == 31:
                day_printed = str(day) + "st"
            if day == 2 or day == 22:
                day_printed = str(day) + "nd"
            if day == 3 or day == 23:
                day_printed = str(day) + "rd"
            elif day != 1 and day != 2 and day != 3 and day != 21 and day != 22 and day != 23 and day != 31:
                day_printed = str(day) + "th"

            print(month_printed, day_printed, "is a valid date in", year)
            
        else:
            print("This is not a valid date in", year)
            
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            if month == 4:
                month_printed = "April"
            if month == 6:
                month_printed = "June"
            if month == 9:
                month_printed = "September"
            if month == 11:
                month_printed = "November"

            if day == 1 or day == 21:
                day_printed = str(day) + "st"
            if day == 2 or day == 22:
                day_printed = str(day) + "nd"
            if day == 3 or day == 23:
                day_printed = str(day) + "rd"
            elif day != 1 and day != 2 and day != 3 and day != 21 and day != 22 and day != 23:
                day_printed = str(day) + "th"
                
            print(month_printed, day_printed, "is a valid date in", year)
        else:
            print("This is not a valid date in", year)
            
    elif month == 2:
        if 1 <= day <= 28:
            month_printed = "February"
            if day == 1 or day == 21:
                day_printed = str(day) + "st"
            if day == 2 or day == 22:
                day_printed = str(day) + "nd"
            if day == 3 or day == 23:
                day_printed = str(day) + "rd"
            elif day != 1 and day != 2 and day != 3 and day != 21 and day != 22 and day != 23:
                day_printed = str(day) + "th"
            print(month_printed, day_printed, "is a valid date in", year)
        else:
            print("This is not a valid date in", year)
            
    else:
        print("This is not a valid date in", year)
