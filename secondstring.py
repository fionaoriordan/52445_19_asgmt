# Fiona O'Riordan 2 March 2019
# Write a program that takes a user input string and outputs every second word




# the user is asked to input a sentence. The string entered is assigned to new value usersentence
usersentence = input('Please enter a sentence:')


#FIRST the python split function  usersentence.split() is used to convert the string usersentence into a list 
#Example: the string 'Daisy Jane Walsh O'Riordan is really great.' inputed by the user is converted into a list of values
# ['Daisy', 'Jane', 'Walsh', 'is', 'really', 'great.']
#NEXT every second value in the list is returned using [::2] 
# because the first colon means start at the first value, the second colon means end at the last value in the list
# but the 2 means return only every second value
#Resulting in: ['Daisy', 'Walsh', 'really']
#Lastly the python join function is used to convert the edited list to a string with delimiter " " to separate each word.
print(" ".join(usersentence.split()[::2]))

