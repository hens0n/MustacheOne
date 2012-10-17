#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup

def GetDomainInfo(Domain):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://toolbar.netcraft.com/site_report?url='+Domain).read())
	theTables = soup.findAll(attrs={"class" : "TBtable"})
	
	if len(theTables) >0:
		basicTable = theTables[0]
		rows = basicTable.findAll('tr')
		for row in rows:
			cols = row.findAll('td')
			if cols[0].b.renderContents().strip() != "Check another site:":
				if  cols[1].a != None:
					print(cols[0].b.renderContents().strip()+ ":" + cols[1].a.renderContents().strip())	
				else:
					print(cols[0].b.renderContents().strip()+ ":" + cols[1].renderContents().strip())

				if  cols[3].a != None:
					print(cols[2].b.renderContents().strip()+ ":\t" + cols[3].a.renderContents().strip())
				else:
					print(cols[2].b.renderContents().strip()+ ":\t" + cols[3].renderContents().strip())	
	if len(theTables) >1:
		print("")
		print("")
		print("Hosting History")
		historyTable = theTables[1]
		rows = historyTable.findAll('tr')

		for row in rows:
			headers = row.findAll('th')
			if len(headers) ==5:
				print(headers[0].get_text() + "\t\t"+ headers[1].get_text() + "\t\t"+ headers[2].get_text()+ "\t\t"+ headers[3].get_text()+ "\t\t"+ headers[4].get_text())
			cols = row.findAll('td')
			if len(cols) ==5:
				print(cols[0].get_text() + "\t\t"+ cols[1].get_text() + "\t\t"+ cols[2].get_text()+ "\t\t"+ cols[3].get_text()+ "\t\t"+ cols[4].get_text())

def PrintHeader():
	header ="""         
************************
NetCraft
http://news.netcraft.com/
************************
	"""
	print(header)