#PL

#!/usr/bin/env python

import socket

network = '192.168.1'

for i in range(1, 256):
   ip = network + '.' + str(i)
   for port in range(1, 65536):
       try:
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.settimeout(0.1)
           result = sock.connect_ex((ip, port))
           if result == 0:
               print(f"Port {port} is open on {ip}")
           sock.close()
       except:
           pass
