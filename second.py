# Fiona O'Riordan 13 Mar 19
# Question 9
# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.
# python second.py moby-dick.txt
# Title:  Moby Dick; or The Whale
# CHAPTER 1
# Call me Ishmael.  Some years ago--never mind how long
# particular to interest me on shore, I thought I would sail about a
# ...
# 1. https://stackoverflow.com/a/37890826
# 2. https://stackoverflow.com/questions/1403674/pythonic-way-to-return-list-of-every-nth-item-in-a-larger-list
# 3. https://docs.python.org/2/library/sys.html#sys.argv
# 4. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# import sys library so that we can use function sys.argv 
import sys

# if two arguments are entered by the user i.e. the program name and the file name 
if len(sys.argv) == 2:
    # then the textfile name is set to be the value of the second argument entered 
    textfile = sys.argv[1]

    with open(textfile,'r+') as f1:
        readfile = f1.read()
        # Firstly, the readfile is split into a list with the endline marker '\n' used to indicate the separate values 
        # Next, every second value in the list is selected
        # Lastly, the selected values are printed as output with an endline value of '\n' placed after each value 
        print('\n'.join(readfile.split('\n')[::2])) 
# Otherwise the user is given advise     
else: 
    print('You should resubmit the program and enter a single file name')
     

  



   

       
       

        