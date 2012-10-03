#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime
import sys

import ipvoid
import networksolutions

def ReportHeader(query):
	now = datetime.datetime.now()
	print("Report for " + query)
	print(now)
	print("==========================================================")

def IsIp(query):
	#regex
	return True

def main(argv):
	if len(argv)==0:
		print("Please provide an argument")
		print("Single URL usage: MustacheOne.py github.com")
		print("Single IP usage: MustacheOne.py 208.78.70.16")

	for arg in argv:
		ReportHeader (arg)
		if IsIp(query):
			ipvoid.GetIpInfo(IP)
			networksolutions.GetIpInfo(IP)


	

if __name__ == "__main__":
   main(sys.argv[1:])

