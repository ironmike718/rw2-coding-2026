"""
name:  dnspy.py
date:  02.25.26
descr: dns lookup tool
"""

# imports
import socket, sys

# ask the user for input
choice = input("DNS Lookup (f)orward or (r)everse? ")

if choice.lower() == "f":
    domain = input("Enter domain: ")
    ipaddr = socket.gethostbyname(domain)
    print(f"{domain} resolves to {ipaddr}\n")
elif choice.lower() == "r":
    ipaddr = input("Enter IP address: ")
    domain = socket.gethostbyaddr(ipaddr)
    print(f"{ipaddr} resolves to {domain[0]}")
else:
    sys.exit(0)
