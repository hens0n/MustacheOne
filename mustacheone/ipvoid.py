#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup



def PrintHeader():
	header ="""         
************************
IP Void
https://www.ipvoid.com
************************
	"""
	print(header)
def GetIpInfoPost(IP):
	PrintHeader()
	url = 'http://www.ipvoid.com/scan/'+IP + '/'
	values = {'url' : IP, 'go':'Scan Now'}

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()

	soup = BeautifulSoup(the_page)
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

def GetIpInfoGet(IP):
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