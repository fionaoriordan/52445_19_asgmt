# Fiona O'Riordan, Created 3-Mar-19
#Solution to Question 8
# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
# Adapted from Python Tutorial 10.8. Dates and Times https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
# and https://stackoverflow.com/questions/46504954/converting-time-to-am-pm-using-python
from datetime import datetime

rightnow = datetime.now()

print(rightnow.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
print(rightnow.strftime("%A, %B %d'something' %Y at %H:%M %p"))


# Open issues Monday 04th March-2019
# 1. Need to include way to return st, nd, rd, th depending on the value of %d
# 2. Need to include way to return pm instead of PM and similarly with AM
# 3. Condense code



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
