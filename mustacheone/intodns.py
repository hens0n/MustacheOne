#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2
import string

sys.path.append('libs/')
from bs4 import BeautifulSoup

def get_header():
	rtn = """
intoDNS
-------
[intoDNS Website](http://www.intodns.com)

"""
	return rtn

def get_info(inquery):
	if inquery.__class__.__name__ == 'IP':
		html = get_html_ip(inquery.address)
		rtn = get_elements(html)
		return rtn
	if inquery.__class__.__name__ == 'URL':
		html = get_html_url(inquery.address)
		rtn = get_elements(html)
		return rtn
def get_html_ip(ip):
	rtn = """
	intoDNS does not let you query ips.

	"""
	return rtn
def get_html_url(url):
	html = urllib2.urlopen('http://www.intodns.com/'+url).read()
	return html
def get_elements(html):
	rtn = ""
	soup = BeautifulSoup(html.decode('ascii','ignore'))
	theTable = soup.find("table", {"class":"tabular"})
	if theTable != None:
		rows = theTable.findAll('tr')
		for row in rows:
			cols = row.findAll('td')
			if len(cols) > 0:
				contents =""
				if cols[0].has_key('rowspan'):
					rtn += ("###%s\n" %(cols[0].renderContents().strip()))
					rtn += ("####%s\n" %(cols[2].renderContents().strip()))
					#contents = ''.join(cols[3].findAll(text=True))
					contents = cols[3].get_text().strip()
				else:
					#rtn += ("##%s\n" %(cols[2].renderContents().strip()))
					#contents = ''.join(cols[2].findAll(text=True))
					contents = cols[2].get_text().strip()
				
				if len(contents) > 0:
					contents = contents.replace("\n","|||")
					lines =contents.replace("\t\n","").replace("  ","").replace("\t","").replace("  ","")
					if ":" in lines:
						lines2= string.split(lines, ':')
						rtn += ("* %s:\n" %(lines2[0]))
						for line in string.split(lines2[1], '|||'):
							if len(line.strip()) >0:
								rtn += ("* %s\n" %(line))
					else:
						for line in string.split(lines, '\n'):
							if len(line.strip()) > 0:
								# print '>>' + line
								rtn += ("* %s\n" %(line))
	else:
		rtn += ("Unable to find data in page.")
	return rtn