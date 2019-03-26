#   MODULE 52445 2019 PROBLEM SET SOLUTIONS
This repository contains the solutions to Module 52445 Problem Set 2019.

## Prerequisites to running the solutions

### 1. Launch your Command Line Interface
1. For Mac users this is Terminal.  Click on the 'LaunchPad' icon in Dock. Click on the folder 'Other'. Click on 'Terminal' icon. Terminal interface is launched.
1.  For Windows the default command line interface is Command Prompt. 
However, CMDER is strongly recommended here.  To install go to: https://cmder.net
1. For Linux users invoke Linux.  For more information please see:https://www.forbes.com/sites/jasonevangelho/2018/11/19/beginners-guide-how-to-install-ubuntu-linux-18-10/#73ebe78e787d

### 2. Install Python  
1. Go to :https://www.anaconda.com/distribution/#download-section 
1. Click on Python 3.7 version 'Download' (using 64 bit option is preferable)
1. Once the download has completed, click on the the Anaconda exe file in Downloads folder. 
1. In the installer window click next and then accept all defaults except do check 'Add Anaconda to my PATH environment variables. Click install.  
1. Launch your command line interface as per above. 
1. At the prompt type 'Python --version' to verify the installation is complete and the version installed e.g. Python 3.7.2

### 3. Install GIT
1. Go to https://git-scm.com/downloads
1. The platform you are using should be detected and the appropriate download link for  MAC OS X, Windows, Linux/Unix should be available to click on. e.g. 'Download 3.20.1 for Windows' button is displayed. 
1. Once the download is complete. Click on the Git exe file in the Downloads folder. Click on next right the way through accepting the defaults presented and finally install.  
1. In your command line interface type 'GIT --version' to verify the install is complete and the version installed e.g. Fionas-Air:52445_19_asgmt fionaoriordan$ git --version
git version 2.20.1

## Repository Contents and Overview of each Solution
1. [sumupto.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/sumupto.py) contains my solution to Question 1. The program asks the user to input any positive integer and outputs the sum of all numbers between one and that number. 
1. [begins-with-t.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/begins-with-t.py) contains my solution to Question 2. The program outputs whether or not today is a day that begins with the letter T.
1. [divisors.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/divisors.py) contains my solution to Question 3. The program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
1. [collatz.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/collatz.py) contains my solution to Question 4. The programme asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. The program ends if the current value is one.
1. [primes.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/primes.py) contains my solution to Question 5. This program asks the user to input a positive integer and tells the userwhether or not the number is a prime.
1. [secondstring.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/secondstring.py) contains my solution to Question 6. This program takes a user input string and outputs every second word.
1. [squareroot.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/squareroot.py) contains my solution to Question 7. This program takes a positive floating point number as input and outputs an approximation of its square root.
1. [fionadatetime.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/fionadatetime.py) contains my solution to Question 8. This program outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.
1. [second.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/second.py) contains my solution to Question 9. This program reads in a text file and outputs every second line. The program takes the filename from an argument on the command line. The file moby-dick.txt contains Chapter1 of mobydick main but body of text/paragraph does not have an endline character in a Mac. The file moby-dickfixed.txt  is an attempt to fix moby-dick.txt that did not work.  See open issues below.
1. [plotfx.py](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/plotfx.py) contains my solution to Question 10. The program displays a plot of the functions x, x2 and 2x in the range [0, 4].

## Executing the solutions
1. In the [repository page 52445_19_asgmt](https://github.com/fionaoriordan/52445_19_asgmt) click on ![download Zip](https://github.com/fionaoriordan/52445_19_asgmt/blob/master/image_downloadzip.png).
1. Once the repository has been saved to your downloads folder locally, then move to your desktop.
1. Launch your Command Line Interface (see above).
1. Open the Desktop directory with command: cd Desktop
1. Open the folder 52445_19_asgmt with command: cd 52445_19_asgmt
1. To run a script type python followed by the script name at the command line prompt e.g. python sumupto.py
1. In the case of Question second.py, at the command line prompt, the programme expects a text file name also to be entered. i.e. python second.py moby-dickfixed.txt


## Open Issues:
1. Question 9:
Mac txt files do not wrap and there appears to be no endline character.  For example when I copy and paste the moby dick text into a txt file on a mac.  The  file recognises the Chapter1 heading and 'Loomings' subheadings and breaks appropriately but the rest of the text is one endless string. 

I tried the following in terminal: file moby-dick.txt
and the result was moby-dick.txt: UTF-8 Unicode text, with very long lines

I tried the following in terminal (based on advise in https://confluence.qps.nl/fledermaus/questions-answers/other/differences-in-end-of-line-characters-mac-windows-and-linux)

sed -e '1,$s/\r$/\r\n/' < moby-dick.txt > moby-dickfixed.txt

Then I ran the following script in terminal ( I was trying all variations of endline that I could find)::


with 
open('moby-dickfixed.txt','r+')
as f:

readfile = f.read()

print(readfile.split('\n'))

print(readfile.split('\r\n'))

print(readfile.split('\r'))

But in the output the paragraph of text is still not split. I have finished the script assuming that the endline character '\n' exists within the text and have modified the text files to include sentences I have manually keyed and manually a return carriage to generate some endline characters '\n'. in order to test the script works when '\n' endline characters exist.

## References
1. Python Documentation 3.7.3rc1 Tutorial 10.8. Dates and Times 
https://docs.python.org/3/tutorial/stdlib.html#dates-and-times
2. Python Documentation 3.7.3rc1 Tutorial 4.1. if Statement  
https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
3. Python Documentation 3.7.3rc1 Tutorial 3.2. First Steps Towards Programming
https://docs.python.org/3.7/tutorial/introduction.html#first-steps-towards-programming
4. Stackoverflow.com Converting time to am/pm using python
https://stackoverflow.com/questions/46504954/converting-time-to-am-pm-using-python
5. Python Documentation 3.7.3rc1 Tutorial 4.2. for Statements
https://docs.python.org/3.7/tutorial/controlflow.html#for-statements
6. Python Documentation 3.7.3rc1 Tutorial 4.4. break and continue Statements, and else Clauses on Loops¶
https://docs.python.org/3.7/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
7. Stackoverflow.com Python - failing to read correctly the first line of a text file to a list
https://stackoverflow.com/a/37890826
8. Stackoverflow.com Pythonic way to return list of every nth item in a larger list, 
 https://stackoverflow.com/questions/1403674/pythonic-way-to-return-list-of-every-nth-item-in-a-larger-list
9. Python Documentation, The Python Standard Library, Python Runtime Services, sys — System-specific parameters and functions,sys.argv
https://docs.python.org/3.7/library/sys.html#sys.argv
10. Python Documentation 3.7.3rc1, Python Tutorials, 7.2. Reading and Writing Files https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
11. Python Documentation 3.7.3rc1, Python Tutorials, 7.2. Built-in Types
https://docs.python.org/3/library/stdtypes.html
12. A Tour of go, Exercise: Loops and Functions
https://tour.golang.org/flowcontrol/8
13. Python Documentation 3.7.3rc1, Python Tutorials 4.1. if Statements
https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
14. Python Documentation 3.7.3rc1, The Language Reference, 2.4.3. Formatted string literals in https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
15. Pandas 0.24.2 Documentation, Getting started, 10 Minutes to Pandas
http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
16. Monterey Institute, Courses, Developtmental Maths, Graphing Types of Functions
https://www.montereyinstitute.org/courses/DevelopmentalMath/TEXTGROUP-15-19_RESOURCE/U17_L2_T2_text_final.html
17. Matplotlib Version 3.03 ,Docs, User's Guide, Tutorials, Pyplot tutorial
https://matplotlib.org/users/pyplot_tutorial.html
18. Scipy.org, Documentation, numby.Arange
https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html
19. Stackoverflow.com, 'How to plot y=1/x as a single graph "duplicate"'
https://stackoverflow.com/questions/44041021/how-to-plot-y-1-x-as-a-single-graph




