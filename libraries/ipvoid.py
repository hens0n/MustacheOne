#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2
from bs4 import BeautifulSoup



def PrintHeader():
	header ="""         
 ___________ _   _       _     _ 
|_   _| ___ \ | | |     (_)   | |
  | | | |_/ / | | | ___  _  __| |
  | | |  __/| | | |/ _ \| |/ _` |
 _| |_| |   \ \_/ / (_) | | (_| |
 \___/\_|    \___/ \___/|_|\__,_|
	https://www.ipvoid.com
	"""
	print(header)

def GetIpInfo(IP):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.ipvoid.com/scan/'+IP+'/').read())
	theTRs = soup.find_all("tr")
	for tr in theTRs:
		temp =""
		cols = tr.findAll('td')
		if len(cols) == 2:
			temp += cols[0].find(text=True)
			temp += " "
			temp += cols[1].find(text=True)
		if len(cols) == 4:
			temp += cols[0].find(text=True)
			temp += ": "
			temp += cols[2].contents[2].contents[0]
		print(temp)