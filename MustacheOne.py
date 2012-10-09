#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime
import sys
import socket

import libraries
from mustacheone import ipvoid
from mustacheone import networksolutions
from mustacheone import projecthoneypot
from mustacheone import robtex

def ReportHeader(query):
	now = datetime.datetime.now()
	print("==========================================================")
	print("Report for " + query)
	print(now)
	print("==========================================================")

def IsIp(query):
	try:
		socket.inet_aton(query)
		return True
	except socket.error:
		return False

def main(argv):
	if len(argv)==0:
		print("Please provide an argument")
		print("Single URL usage: MustacheOne.py github.com")
		print("Single IP usage: MustacheOne.py 208.78.70.16")
		print("Combination usage: MustacheOne.py github.com 208.78.70.16 google.com")

	for arg in argv:
		ReportHeader (arg)
		if IsIp(arg):
			#ipvoid.GetIpInfo(arg)
			networksolutions.GetIpInfo(arg)
			#projecthoneypot.GetIpInfo(arg)
			#robtex.GetIpInfo(arg)
		else:
			networksolutions.GetDomainInfo(arg)



	

if __name__ == "__main__":
   main(sys.argv[1:])

