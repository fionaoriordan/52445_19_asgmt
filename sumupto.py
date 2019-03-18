#Fiona O'Riordan 
#Created 12 Feb 2019
#Module 52445 Problem Set, Question 1 
#Write a program that asks the user to input any positive integer 
# and outputs the sum of all numbers between one and that number.

# Adapted from:
# 1. https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
# 2. 2.4.3. Formatted string literals in https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals

# assign the value entered by the user to i 
i = int(input('Please enter a positive integer:' ))
# remember the original number entered.
num = i

# if the number entered is not a positive integer 
if i < 1 :
    # then tell the user and take no more actions.
    print(f"{i} is not a positive integer.\nPlease enter a positive integer the next time you execute this script.")
    # Otherwise begin calculating the sum of all the numbers between one and the number entered.
else: 
    # set the answer = the number entered 
    ans = i
    # loop while the last number added to the answer is greater than or equal to 1
    while i >= 1:
        # increment the answer by adding a number one less than the number entered/added during the last loop
        ans = ans + (i-1)
        # decrease the number entered by 1
        i = i-1
    # print the answer
    print(f"The sum of all the numbers between {num} and 1 is {ans}.")


