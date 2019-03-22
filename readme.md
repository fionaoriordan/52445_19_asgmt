#   MODULE 52445 2019 PROBLEM SET SOLUTIONS
This repository contains the solutions to Module 52445 Problem Set 2019.

## Prerequisites to running the solutions

### 1. Launch your Command Line Interface
    1. For Mac users this is Terminal.  Click on the 'LaunchPad' icon in Dock. Click on the folder 'Other'. Click on 'Terminal' icon. Terminal interface is launched.
    1.  For Windows the default command line interface is Command Prompt. 
However, CMDER is strongly recommended here.  To install and launch go to: https://cmder.net
    1. For Linux users invoke Linux.  For more information please see:https://www.forbes.com/sites/jasonevangelho/2018/11/19/beginners-guide-how-to-install-ubuntu-linux-18-10/#73ebe78e787d

#### 2. Install Python  
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


## Repository Contents

1. sumupto.py contains my solution to Question 1 
2. begins-with-t.py contains my solution to Question 2
3. divisors.py contains my solution to Question 3
4. collatz.py contains my solution to Question 4
5. primes.py contains my solution to Question 5
6. secondstring.py contains my solution to Question 6
7. squareroot.py contains my solution to Question 7
8. fionadatetime.py contains my solution to Question 8 myfile.txt contains Chapter1 of mobydick for Question but has no endline character in a mac. myfilefixed.txt is myfilefixed.txt is an attempt to fix myfile.txt that did not work.  See open issues.
9. second.py contains my solution to Question 9
10. plotfx.py contains my solution to Question 10


## Executing the solutions

## Open Issues:
1. Question 9:
Mac txt files do not wrap and there appears to be no endline character.  For example when I copy and paste the moby dick text into a txt file on a mac.  The  file recognises the Chapter1 heading and 'Loomings' subheadings and breaks appropriately but the rest of the text is one endless string. 

I tried the following in terminal: file myfile.txt
and the result was myfile.txt: UTF-8 Unicode text, with very long lines

I tried the following in terminal (based on advise in https://confluence.qps.nl/fledermaus/questions-answers/other/differences-in-end-of-line-characters-mac-windows-and-linux)

sed -e '1,$s/\r$/\r\n/' < myfile.txt > myfilefixed.txt

Then I ran the following script in terminal ( I was trying all variations of endline that I could find)::


with 
open('myfilefixed.txt','r+')
as f:

readfile = f.read()

print(readfile.split('\n'))

print(readfile.split('\r\n'))

print(readfile.split('\r'))

But in the output the paragraphy of text is still not split. I have finished the script assuming that the endline character '\n' exists within the text.

## References
1. Python Documentation Tutorial 10.8. Dates and Times 
 (https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)
2. Python Documentation Tutorial 10.8. Dates and Times  
https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
3. https://docs.python.org/3.7/tutorial/introduction.html#first-steps-towards-programming
4. https://stackoverflow.com/questions/46504954/converting-time-to-am-pm-using-python
https://docs.python.org/3.7/tutorial/controlflow.html#for-statements
5.
5. https://docs.python.org/3.7/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
6. https://stackoverflow.com/a/37890826
7. https://stackoverflow.com/questions/1403674/pythonic-way-to-return-list-of-every-nth-item-in-a-larger-list
8. https://docs.python.org/2/library/sys.html#sys.argv
9. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
10. https://docs.python.org/3/library/stdtypes.html
11. https://tour.golang.org/flowcontrol/8
12. https://docs.python.org/3.7/tutorial/controlflow.html#if-statements
13. 2.4.3. Formatted string literals in https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
14. http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
15. https://www.montereyinstitute.org/courses/DevelopmentalMath/TEXTGROUP-15-19_RESOURCE/U17_L2_T2_text_final.html
16. https://matplotlib.org/users/pyplot_tutorial.html
17. https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html
18. https://stackoverflow.com/questions/44041021/how-to-plot-y-1-x-as-a-single-graph




