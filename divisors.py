# Fiona O'Riordan, 28-FEB-19
# Question 1 Write a program that prints all numbers between 1,000 and 10,000 
# that are divisible by 6 but not 12.
# Assumption: between 1,000 and 10,000 is inclusive of both values

# set i equal to 1000 in order to begin at that value 
i = 1000 

# loop until number 10000 is tested.
while i <= 10000:
    # test if i is evenly divisible by 6 but not 12
    if (i%6 == 0) and (i%12 != 0):
        # print the number that is true for both conditions to the screen 
        print(i)
    # increment value of i by 1 in order to test the next number 
    i = i+1
