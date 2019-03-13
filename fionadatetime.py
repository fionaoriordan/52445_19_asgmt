# Fiona O'Riordan, Created 3-Mar-19
#Solution to Question 8
# Write a program that outputs today’s date and time in the format
#  ”Monday, January 10th 2019 at 1:15pm”.
# Adapted from Python Tutorial 10.8. Dates and Times https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
# and https://stackoverflow.com/questions/46504954/converting-time-to-am-pm-using-python

from datetime import datetime 

# rightnow = datetime.now()

# print(rightnow.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# print(rightnow.strftime("%A, %B %d'something' %Y at %H:%M %p"))

# Creating a function which reads an integer value and outputs the value 
# as a string with appropriate suffix st, nd, rd or th
def nth(day):
# set suffix = 'th' for all days btwn 11 and 20
    if day > 10 and day < 20: 
        suffix = 'th'
# set suffix for all other numbers based on 
# thelast digit in the day
    else:   
        unit = str(day)
        unit = unit[-1]
        if unit == "1": 
            suffix = 'st'
        elif unit == "2":
            suffix = 'nd'
        elif unit == "3":
            suffix = 'rd'
        else:
            suffix = 'th'
    return str(day)+ suffix

# dayord is todays date in the format nth e.g. 25th
dayord = nth(int(datetime.now().strftime("%d")))
daymonth = datetime.now().strftime("%A, %B") 
year = datetime.now().strftime("%Y") 
time = datetime.now().strftime("%-I:%M")
ampm = datetime.now().strftime("%p").lower()

print(f"{daymonth} {dayord} {year} at {time}{ampm}")






# 03 Mar-19 
# 1. Note: when the python file was named datetime.py then the following error message was displayed in terminal
# 
# Fionas-MacBook-Air:52445_19_asgmt fionaoriordan$ python datetime.py
# Traceback (most recent call last):
#   File "datetime.py", line 4, in <module>
#     from datetime import date
#   File "/Users/fionaoriordan/Desktop/52445_19_asgmt/datetime.py", line 4, in <module>
#     from datetime import date
# ImportError: cannot import name 'date' from 'datetime' (/Users/fionaoriordan/Desktop/52445_19_asgmt/datetime.py)
# Fionas-MacBook-Air:52445_19_asgmt fionaoriordan$ 

# 03-Mar-19
# 2. When I changed the file name from datetime.py (as specified in Problem Set 2019, Question 9) to fionadatetime.py 
# the issue was resolved. I assume the conflict arose when the libray name datetime was used as a file name. 
