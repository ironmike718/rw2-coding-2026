#!/usr/bin/python3

import os, subprocess

userInput = input("What is your name? ")

if userInput == "mike":
    role = "teacher"
else:
    role = "student"

counter = 1
while counter <= 3:
    if role == "teacher":
        print("Life is great!")
    else:
        print("Life is tough")
    counter +=1

# opening a file w/ python

myNameFile = open("names.txt")

#print(myNameFile.read())

counter = 1
for line in myNameFile:
    aLine = line.strip()
    if aLine == "Brandon":
        print(f"the name on line-{counter} is {aLine}")
    else:
        print(f"the name is not Brandon, it's {aLine}")
    counter += 1

# how to use imports

# capture the date from linux command line

#os.system("date")

myDate = subprocess.run(["date"])

print(f"today's date from linux is:  {myDate}")






