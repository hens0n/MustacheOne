#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2
from bs4 import BeautifulSoup


def PrintHeader():
	header ="""         
 _   _      _                      _     _____       _       _   _                 
| \ | |    | |                    | |   /  ___|     | |     | | (_)                
|  \| | ___| |___      _____  _ __| | __\ `--.  ___ | |_   _| |_ _  ___  _ __  ___ 
| . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ / `--. \/ _ \| | | | | __| |/ _ \| '_ \/ __|
| |\  |  __/ |_ \ V  V / (_) | |  |   < /\__/ / (_) | | |_| | |_| | (_) | | | \__ \\
\_| \_/\___|\__| \_/\_/ \___/|_|  |_|\_\\\\____/ \___/|_|\__,_|\__|_|\___/|_| |_|___/
	http://www.networksolutions.com
	"""
	print(header)

def GetIpInfo(IP):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.networksolutions.com/whois/results.jsp?ip='+IP).read())
	thePreTag = soup.find("pre")
	print(thePreTag.string)

def GetDomainInfo(Domain):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.networksolutions.com/whois-search/'+Domain).read())
	theSummary = soup.find("div", {"class":"summary"})
	rows = theSummary.findAll('tr')
	for row in rows:
		cols = row.findAll('td')
		if type(cols[1].string).__name__ !=  'NoneType':
			print(cols[0].string + ' ' +cols[1].string.strip())