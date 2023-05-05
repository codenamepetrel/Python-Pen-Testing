#!/usr/bin/env python

import socket

# Get the hostname of the local machine
hostname = socket.gethostname()

# Get the IP address of the local machine
ip_address = socket.gethostbyname(hostname)

# Print the IP address and save it into a variable
print("My IP address is:", ip_address)
my_ip = ip_address
