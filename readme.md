#   MODULE 52445 2019 PROBLEM SET SOLUTIONS
This repository contains the solutions to Module 52445 Problem Set 2019.

## Prerequisites to running the solutions

### Install GIT
1. Go to GITHub
2. 

#### Install Python
1. Go to 
2. Click on

## Repository Contents

1. sumupto.py contains my solution to Question 1 
2. begins-with-t.py contains my solution to Question 2
3. divisors.py contains my solution to Question 3
4. collatz.py contains my solution to Question 4
5. primes.py contains my solution to Question 5
6. secondstring.py contains my solution to Question 6
7. squareroot.py contains my solution to Question 7
8. fionadatetime.py contains my solution to Question 8
myfile.txt contains Chapter1 of mobydick for Question but has no endline character in a mac. myfilefixed.txt is myfilefixed.txt is an attempt to fix myfile.txt that did not work.  See open issues.
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
