"""
name:  cyber-port-game.py
date:  02.25.26
rev:   1
descr: use python to create cli port # guessing game
"""
# modules to import

import random, os, time, sys

# variables

banner = "\n\n ### Cyber Port Number Guessing Game ### \n\n"
svc_names = ["SSH", "HTTP", "HTTPS", "Telnet", "RDP", "VNC", "POP3", "SMTP", "DNS", "DHCP"]
port_nums = [22, 80, 443, 23, 3389, 5900, 110, 25, 53, 67]
score = 0

# generate random integer list from 0 to 9
# use them to access the svc_names and port_nums elements

ran_int_list = random.sample(range(0, 10), 10)

# print the banner

os.system("clear")
print(banner)

# loop through the random integer list
# get user input, validate user input

for num in ran_int_list:
    user_guess = input(f"What port # does the {svc_names[num]} service run on?  ")
    user_guess = int(user_guess)
    #
    if user_guess == port_nums[num]:
        print(f"correct -- {svc_names[num]} run on port # {port_nums[num]}")
        score =+ 1
    else:
        print(f"sorry -- {svc_names[num]} run on port # {port_nums[num]}")

# calculate the score

grade = round((score / len(port_nums) * 100), 2)

# print final message

print(f"\n\nYou got {score} correct answers of {len(port_nums)}! Your grade is {grade}%\nKeep Practicing!!!\n")
