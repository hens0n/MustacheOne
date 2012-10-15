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
************************
Project Honey Pot
http://www.projecthoneypot.org
************************
	"""
	print(header)
