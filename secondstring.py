# Fiona O'Riordan 2 March 2019
# Module 52445 Problem Set, Solution to Question 6 
# Write a program that takes a user input string and outputs every second word

# Adapted from:
# 1. https://docs.python.org/3/library/stdtypes.html

# the user is asked to input a sentence. The string entered is assigned to new value usersentence
usersentence = input('Please enter a sentence:')

#FIRST the python split function  usersentence.split() is used to convert the string usersentence into a list of values
# ['Daisy', 'Jane', 'Walsh', 'is', 'really', 'great.']
#NEXT every second value in the list is returned using [::2] 
# because the first colon means start at the first value, the second colon means end at the last value in the list
# but the 2 means return only every second value
#LASTLY the python join function is used to convert the edited list to a string with delimiter " " to separate each word.
print(" ".join(usersentence.split()[::2]))

