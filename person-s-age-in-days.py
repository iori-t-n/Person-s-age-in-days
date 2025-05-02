"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    date1 = datetime.date(year, month, 1)
    if 0 <= month < 12:
        date2 = datetime.date(year, month + 1, 1)
    else:
        date2 = datetime.date(year + 1, 1, 1)
    
    difference = date2 - date1
    return difference.days

## Test days_in_month function.
#print (days_in_month(2025, 12))


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if (year < datetime.MINYEAR) or (year > datetime.MAXYEAR):
        return False
    elif (1 <= month <= 12) and (1 <= day <= days_in_month(year, month)):
        return True
    else:
        return False

## Test is_valid_date function.
#print (is_valid_date(2025, 1, 32))

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if (is_valid_date(year1, month1, day1) == True) and (is_valid_date(year2, month2, day2)):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        difference = date2 - date1
        if date2 >= date1:
            return difference.days
        else: 
            return 0
    else:
        return 0  
    
##Test days_between(year1, month1, day1, year2, month2, day2) function.
#print(days_between(2024, 1, 1, 2025, 1, 1)) 
#
#todays_date = datetime.date.today()
#print(todays_date)

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    todays_date = datetime.date.today()
    todays_year = todays_date.year
    todays_month = todays_date.month
    todays_day = todays_date.day
    
    return days_between(year, month, day, todays_year, todays_month, todays_day)
    
##Test age_in_days(year, month, day)function
#print(age_in_days(2024, 4, 21))
    