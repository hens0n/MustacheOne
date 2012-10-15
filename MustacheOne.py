#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime
import sys
import socket
import ConfigParser


from mustacheone import ipvoid
from mustacheone import networksolutions
from mustacheone import projecthoneypot
from mustacheone import robtex
from mustacheone import virustotal

def ReportHeader(query):
	header ="""
___  ___          _             _           _____            
|  \\/  |         | |           | |         |  _  |           
| .  . |_   _ ___| |_ __ _  ___| |__   ___ | | | |_ __   ___ 
| |\\/| | | | / __| __/ _` |/ __| '_ \\ / _ \\| | | | '_ \\ / _ \\
| |  | | |_| \\__ \\ || (_| | (__| | | |  __/\\ \\_/ / | | |  __/
\\_|  |_/\\__,_|___/\\__\\__,_|\\___|_| |_|\\___| \\___/|_| |_|\\___|                                                            
    https://github.com/cyberphilia/MustacheOne
"""
	now = datetime.datetime.now()
	print(header)
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

def getConfig(section, name):
	try:
		config = ConfigParser.RawConfigParser()
		config.read('config.ini')
		rtn = config.get(section,name)
		return rtn
	except ConfigParser.NoSectionError:
		print("Section Not Found")
	except ConfigParser.NoOptionError:
		print("Option Not Found")

def main(argv):
	if len(argv)==0:
		print("Please provide an argument")
		print("Single URL usage: MustacheOne.py github.com")
		print("Single IP usage: MustacheOne.py 208.78.70.16")
		print("Combination usage: MustacheOne.py github.com 208.78.70.16 google.com")
	
	

	for arg in argv:
		ReportHeader (arg)
		if IsIp(arg):
			ipvoid.GetIpInfoPost(arg)
			networksolutions.GetIpInfo(arg)
			projecthoneypot.GetIpInfo(arg)
			#robtex.GetIpInfo(arg)
		else:
			networksolutions.GetDomainInfo(arg)
			virustotalkey= getConfig("virustotal","apikey")
			if virustotalkey != None:
				virustotal.GetUrlReport(arg,virustotalkey)
			else:
				print("****You will need to put your Virus Total API key in config.ini.  Review the README")



	

if __name__ == "__main__":
   main(sys.argv[1:])

