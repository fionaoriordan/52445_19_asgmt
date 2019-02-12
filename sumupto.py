#Fiona O'Riordan 52445 Assigment 1 
#Created 12 Feb 2019
#Write a program that asks the user to input any positive integer 
# and outputs the sum of all numbers between one and that number.
#python sumupto.py
#Please enter a positive integer: 10
#55

# 12 Feb 2019: While this solution works, it is not entirely satisfactory as:
# 1)the standard exception message raised when handling a string entered by the
# user need to be replaced by a more user friendly message
# 2) and then after the float has been entered another opportunity for the user 
# to enter a postive integer also needs to be included. 
# 3) research is need to find if a more efficent method to handle floats, 
# zero and negative integers could be used.
# 4)lastly, some yet unknown requirements/ improvements may be discovered.

i = int(input('Please enter a postive integer:' ))

while i < 1:
    if i == 0:
        i = int(input('Zero is not positive. Please enter a postive integer:' ))
    elif i < 0:
        i =  i = int(input('Please enter a postive integer, a number greater than 0:' ))   

ans = i
while i >= 1:
    ans = ans + (i-1)
    i = i-1

print(ans)