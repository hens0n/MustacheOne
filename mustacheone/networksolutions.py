#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2

from bs4 import BeautifulSoup

def PrintHeader():
	header ="""         
************************
Network Solutions
http://www.networksolutions.com
************************
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
			
	theContent = soup.find("div", {"class":"content"})
	thetable = theContent.find("table")
	theSubTable = thetable.find("table")
	cols = theSubTable.findAll('td')
	for col in cols:
		c = col.renderContents().strip()
		if len(c) > 4	:		
			if col.strong != None:
				
				c = c.replace('\n','')
				c = c.replace('\t','')
				c = c.replace('<strong>','')
				c = c.replace('</strong>','')
				print("")
				print("*"+c)
			elif  col.a != None:
				if 'target' in col.a.attrs and not "underlying" in col.a.renderContents().strip():
					print(col.a.renderContents().strip())
			elif  col.pre != None:
				print(col.pre.renderContents().strip())		
			else:
				print(c.strip())