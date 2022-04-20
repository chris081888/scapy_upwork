#!/usr/bin/env python

import scapy.all as scapy

arp_request = scapy.ARP(pdst="192.168.1.1/24")
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
arp_reqest_broadcast = broadcast/arp_request
answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

clients_list = []

for answer in answered:
	clients_list.append(answer[1].psrc)
	
for client in clients_list:
	print(client)