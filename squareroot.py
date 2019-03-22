# # Fiona O'Riordan, 03 Mar 2019
# Module 52445 Problem Set, Solution to Question 7
# Write a program that that takes a positive floating point number as input and outputs 
# an approximation of its square root.
# Adapted from https://tour.golang.org/flowcontrol/8. 

# import the math library so that we can use the math function sqrt later to 
# verify the below code.
import math
# set num equal to a float number entered by the user
num = float(input('Please enter a positive floating number:' ))

# if the num entered by the user is not positive, ask the user to try again.
if num <= 0:
    print(f"{num} is not a POSITIVE floating number.\nTry again.")
else:
    # set the estimate equal to num/2 to begin with as we must start with
    # some kind of estimate
    estimate = num/2
    # keep looping around until the square of the estimate is within
    # 0.01 of num. This is Newton's estimate method to improve the estimate.
    while abs((estimate * estimate) - num) > 0.01:
        estimate -=((estimate * estimate) - num) / (2 * estimate)
    print(f"The square root of {num} is {estimate} approximately.")
    # To verify the result is sufficiently close, print the math function sqrt of num.  
    print(math.sqrt(num))


 
