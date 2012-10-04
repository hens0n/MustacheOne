#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2
from bs4 import BeautifulSoup

def GetIpInfo(IP):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.projecthoneypot.org/ip_'+IP).read())
	theTag =soup.find("div", { "class" : "contain" })
	thestring = ""
	for child in theTag.contents[3].children:
		thestring +=child.string.encode('ascii', 'ignore')
	print(thestring)
def PrintHeader():
	header ="""         
______           _           _     _   _                         ______      _   
| ___ \         (_)         | |   | | | |                        | ___ \    | |  
| |_/ /_ __ ___  _  ___  ___| |_  | |_| | ___  _ __   ___ _   _  | |_/ /___ | |_ 
|  __/| '__/ _ \| |/ _ \/ __| __| |  _  |/ _ \| '_ \ / _ \ | | | |  __// _ \| __|
| |   | | | (_) | |  __/ (__| |_  | | | | (_) | | | |  __/ |_| | | |  | (_) | |_ 
\_|   |_|  \___/| |\___|\___|\__| \_| |_/\___/|_| |_|\___|\__, | \_|   \___/ \__|
               _/ |                                        __/ |                 
              |__/                                        |___/                  
	http://www.projecthoneypot.org
	"""
	print(header)
