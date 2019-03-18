# Fiona O'Riordan, 28 Feb 2019
# Solution to Question 4
# Write a program that asks the user to input any positive integer and outputs 
# the successive values of the following calculation. At each step calculate 
# the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.
# Adapted from: 
# 1. https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
# 2. https://docs.python.org/3.7/tutorial/introduction.html#first-steps-towards-programming

# assign the value entered by the user to i 
i = int(input('Please enter a positive integer:' ))

# loop while a positive integer has NOT been entered by the user
while i < 1:
    # if zero  entered then inform user and ask them to re-enter 
    if i == 0:
        # assign the new entered to i
        i = int(input('Zero is not positive. Please enter a positive integer:' ))
    # if a negative integer has been entered then inform user and ask them to re-enter    
    elif i < 0:
        i = int(input('Not a postive integer. Please enter a positive integer:' )) 

# loop while i is greater than one, initially i is the number entered
while i > 1:
    # if the current value of i is even
    if (i%2 == 0):
        # then print the number
        print(int(i))
        # and then divide the current value of i  by 2
        i = i/2
    # otherwise if the current value of i number is odd
    else:
        # then print the number
        print(int(i))
        # but then multiply it by three and then add one.
        i = i*3 +1
# lastly print the number which is now at 1.
print(int(i))