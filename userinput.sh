#!/bin/bash

# get user input

echo -n "Give me a number from 1 to 20: "
read num1

echo -n "Give me another number from 1 to 20: "
read num2

# use an if statement
if [ ${num1} -gt ${num2} ]; then
  echo -e "${num1} is > ${num2}\n"
elif [ ${num1} -lt ${num2} ]; then
  echo -e "${num2} is > ${num1}\n"
else
  echo -e "i don't know anything about numbers!\n"
fi

# print user input to the screen
# echo -e "\nYou told me your favorite food is ${favFood} and favorite drink is ${favDrink}\n"

exit 0
