# Fiona O'Riordan, 28 Feb 2019
# Solution to Question 5
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.

# Verbatim from https://whatis.techtarget.com/definition/prime-number:
# 'A prime number is a whole number greater than 1 whose only factors are 1 and itself.'
 

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

if i > 1:
   # loop to check for factors. begin with 2 as a factor and then stop at i 
    for j in range(2, i):
        # if i can be divided evenly by j then it is not a factor
        if (i % j) == 0:
            print(i,"is not a prime number")
            break
    else:
         print("That is a prime number")
else: 
    print(i, "is not a prime number")


