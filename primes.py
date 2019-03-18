# Fiona O'Riordan, 28 Feb 2019
# 52445 Problem Set,Solution to Question 5
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.

# Verbatim from https://whatis.techtarget.com/definition/prime-number:
# 'A prime number is a whole number greater than 1 whose only factors are 1 and itself.'
# Adapted from:
# 1. https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
# 2. https://docs.python.org/3.7/tutorial/controlflow.html#for-statements
# 3. https://docs.python.org/3.7/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# assign the value entered by the user to i 
i = int(input('Please enter a positive integer:' ))
# assign the value 1 to count to record the users first attempt
count = 1

# loop while a positive integer has NOT been entered by the user 
# and they have not made 3 attempts or more. 
while i < 1 and count <=2:
    # if a number equal to or less than zero is entered 
    # then inform user and ask them to re-enter
    i = int(input(f'{i} is not a positive integer. Please enter a positive integer:' ))
    # increment count by 1 so that the user only gets three attempts.
    count = count+1

# If the number is positive integer then check if it is a prime    
if i >= 1:
    # 1 is not a prime number 
    if i ==1:
        print(f"No, {i} is not a prime number.")
   # for positive integers greater other than 1, loop to check for factors. begin with 2 as a factor and then stop at i 
    else:
        for j in range(2, i):
        # if i can be divided evenly by j then it is not a factor
            if (i % j) == 0:
                print(f"No, {i} is not a prime number.")
                # break because if i can be divided evenly by number other than itself or 1 it is not a prime number and so time to stop the loop
                break   
        # if after going right through the range without finding a factor other than 1 or itself then the number entered is a prime number
        else: 
            print(f"Yes, {i} is a prime number.")
# User had had three chances to enter a positve integer. Time to stop.
elif count ==3 : 
        print("You've had 3 chances.\nTime to take a break and think about what is a positive integer.")



