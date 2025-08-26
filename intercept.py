#!/usr/bin/python
from scapy.all import *

# capture = sniff()
sniff(lfilter=lambda x: x.haslayer(UDP) and x.haslayer(DNS),prn=lambda x:x.summary())
