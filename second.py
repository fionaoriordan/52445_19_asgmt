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

# text = input('Please enter the name of your textfile: ' )

# if text[-4:] != '.txt':
#     text = input('Please enter the name of your textfile: ' )
# Adapted from https://stackoverflow.com/a/37890826



# def split_lines(text): 
#     lines = text.split('\n')     
#     return '\n'.join(s.strip()) 


with open('myfilefixed.txt','r+') as f:
    readfile = f.read()
    print(readfile.split('\n'))
    print(readfile.split('\r\n'))
    print(readfile.split('\r'))

# with open('plain2.txt', 'U') as infile:
#     text = infile.read()  # Automatic ("Universal read") conversion of newlines to "\n"
# with open('plain2.txt', 'w') as outfile:
#     outfile.write(text)  # Writes newlines for the platform running the program
    
# if "\r\n" in open("/path/file.txt","rb").read():
#     print("DOS line endings found")

# s = ("Hello World\ngoodbye World\n")
# print(s)
   

       
       

        