#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime
import sys

import ipvoid

def ReportHeader(query):
	now = datetime.datetime.now()
	print("Report for " + query)
	print(now)

def IsIp(query):
	#regex
	return True

def main(argv):
	if len(argv)==0:
		print("Please provide an argument")
		print("IP usage: MustacheOne.py 192.168.1.1")
		print("URL usage: MustacheOne.py google.com")

	for arg in argv:
		ReportHeader (arg)
		if IsIp(query):
			ipvoid.GetInfo(IP)


	

if __name__ == "__main__":
   main(sys.argv[1:])

