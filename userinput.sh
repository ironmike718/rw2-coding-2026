#!/bin/bash

# get user input

echo -n "What is your favorite food? "
read favFood

echo -n "What is your favorite drink? "
read favDrink

# print user input to the screen
echo -e "\nYou told me your favorite food is ${favFood} and favorite drink is ${favDrink}\n"

exit 0
