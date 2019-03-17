# Fiona O'Riordan, 27-FEB-19
# Write a program that outputs whether or not today is a day that begins 
# with the letter T. 
# Adapted from Python Tutorial 10.8. Dates and Times 
# (https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)

# import the date class from the datetime library date functions 
# can be used below 
from datetime import date
# set my date equal to today
my_date = date.today()

# use the strftime function get the actual day name of today e.g. Thursday 
# and if the first letter of today's day name is equal to 'T' then print to 
# confirmation of same
if my_date.strftime('%A')[0] == 'T':
    print('Yes - today begins with a T.' )
# Otherwise print to the screen that today does not begin with T
else:
    print('No - today does not begin with a T.')

