# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

from ipip import IP
from ipip import IPX

f = open("jiangsu.txt")

for line in f:	
	IP.load(os.path.abspath("17monipdb.dat"))
	tmpaddress = IP.find(line).split()
	if len(tmpaddress) == 3:
		address = tmpaddress[2]
		if address == '南京':
			fout = open('out.txt','a') 
			fout.write(line)
f.close()
fout.close()
