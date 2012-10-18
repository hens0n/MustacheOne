#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2
import string

from bs4 import BeautifulSoup

def GetDomainInfo(Domain):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.intodns.com/'+Domain).read())


	theTable = soup.find("table", {"class":"tabular"})
	if theTable != None:
		rows = theTable.findAll('tr')
		for row in rows:
			cols = row.findAll('td')
			if len(cols) > 0:
				contents =""
				if cols[0].has_key('rowspan'):
					print("**********"+cols[0].renderContents().strip()+"**********")
					print("\t***"+ cols[2].renderContents().strip())
					#contents = ''.join(cols[3].findAll(text=True))
					contents = cols[3].get_text().encode('ascii', 'ignore').strip()
				else:
					print("\t***"+cols[1].renderContents().strip())
					#contents = ''.join(cols[2].findAll(text=True))
					contents = cols[2].get_text().encode('ascii', 'ignore').strip()
				
				if len(contents) > 0:
					contents2 =contents.replace("\t\n","").replace("  ","").replace('\n\n', ' ').replace("\t","").replace("  ","")
					for line in string.split(contents2, '\n'):
						if len(line.strip()) > 0:
							print("\t\t"+line)
	else:
		print("Unable to find data in page.")

def PrintHeader():
	header ="""         
************************
intoDNS
http://www.intodns.com/
************************
	"""
	print(header)