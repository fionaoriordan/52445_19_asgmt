# Fiona O'Riordan, 27-FEB-19
# Write a program that outputs whether or not today is a day that begins with the letter T. 
# Adapted from Python Tutorial 10.8. Dates and Times 
# (https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)

from datetime import date

my_date = date.today()

if my_date.strftime('%A')[0] == 'T':
    print('Yes - today begins with a T.' )
else:
    print('No - today does not begin with a T.')

