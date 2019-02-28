# Fiona O'Riordan, 28 Feb 2019
# Solution to Question 4
# Write a program that asks the user to input any positive integer and outputs 
# the successive values of the following calculation. At each step calculate 
# the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

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


while i > 1:
    if (i%2 == 0):
        print(int(i))
        i = i/2
    else:
        print(int(i))
        i = i*3 +1
print(int(i))