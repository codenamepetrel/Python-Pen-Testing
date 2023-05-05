#Pete Lenhart

#!/usr/bin/env python

import socket

network = '192.168.1'
tcp_ports = range(1, 1024)
udp_ports = range(1, 1024)

with open('port_scan_results.txt', 'w') as f:
    for i in range(1, 256):
        ip = network + '.' + str(i)
        for port in tcp_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    f.write(f"TCP Port {port} is open on {ip}\n")
                sock.close()
            except:
                pass
        for port in udp_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                sock.sendto(b'', (ip, port))
                result = sock.recvfrom(1024)
                f.write(f"UDP Port {port} is open on {ip}\n")
                sock.close()
            except:
                pass
