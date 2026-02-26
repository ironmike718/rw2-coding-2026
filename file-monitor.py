"""
name:  file-monitor.py
date:  02.25.26
descr: basic file integrity monitor
"""

# imports
import hashlib, os

# get user input for file to monitor
filename = input("Enter file to monitor: ")

# function to create hash
def hash_file(file):
    h = hashlib.sha256()
    with open(file, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

baseline = hash_file(filename)

print("Monitoring for changes...")

while True:
    current = hash_file(filename)
    if current != baseline:
        print("ALERT -- File changed!!!")
        break