#   MODULE 52445 2019 PROBLEM SET SOLUTIONS
This repository contains the solutions to Module 52445 Problem Set 2019.

## Prerequisites to running the solutions

### 1. Launch your Command Line Interface
 1.1. For Mac users this is Terminal.  Click on the 'LaunchPad' icon in Dock. Click on the folder 'Other'. Click on 'Terminal' icon. Terminal interface is launched.
1.2  For Windows the default command line interface is Command Prompt. 
However, CMDER is strongly recommended here.  To install and launch go to: https://cmder.net
1.3 For Linux users invoke Linux.  For more information please see:https://www.forbes.com/sites/jasonevangelho/2018/11/19/beginners-guide-how-to-install-ubuntu-linux-18-10/#73ebe78e787d

#### 2. Install Python  
2.1 Go to :https://www.anaconda.com/distribution/#download-section 
2.2 Click on Python 3.7 version 'Download' (using 64 bit option is preferable)
2.3 Once the download has completed, click on the the Anaconda exe file in Downloads folder. In the installer click next and then accept all defaults except do check 'Add Anaconda to my PATH environment variables. Click install.  Launch your command line interface as per above. At the prompt type 'Python --version' to verify the installation is complete and the version installed e.g. Python 3.7.2

### 3. Install GIT
3.1 Go to https://git-scm.com/downloads
3.2 The platform you are using should be detected and the appropriate download link for  MAC OS X, Windows, Linux/Unix should be available to click on. e.g. 'Download 3.20.1 for Windows' button is displayed. Once the download is complete. Click on the Git exe file in the Downloads folder. Click on next right the way through accepting the defaults presented and finally install.  In your command line interface type 'GIT --version' to verify the install is complete and the version installed e.g. Fionas-Air:52445_19_asgmt fionaoriordan$ git --version
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
Mac txt files do not wrap and there appears to be no endline character.  For example when I copy and paste the moby dick text into a txt file on a mac.  The  file recognises the Chapter1 heading  'Loomings' and breaks appropriately but the rest of the text is one endless string. 

I tried the following in terminal: file myfile.txt
and the result was myfile.txt: UTF-8 Unicode text, with very long lines

I tried the following in terminal (based on advise in https://confluence.qps.nl/fledermaus/questions-answers/other/differences-in-end-of-line-characters-mac-windows-and-linux)

sed -e '1,$s/\r$/\r\n/' < myfile.txt > myfilefixed.txt

Then I ran the following script in terminal ( I was trying all variations of endline that I could find):
( I was trying all variations of endline that I could find):


with 
open('myfilefixed.txt','r+')
as f:

readfile = f.read()

print(readfile.split('\n'))

print(readfile.split('\r\n'))

print(readfile.split('\r'))

But output is still not split. 

## References
