#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import urllib 
import urllib2
import string

sys.path.append('libs/')
from bs4 import BeautifulSoup
def get_header():
	rtn = """
IP Void
-------
[IP Void Website](https://www.ipvoid.com)

"""
	return rtn
def get_elements(html):
	rtn = ""
	soup = BeautifulSoup(html.decode('ascii','ignore'))
	tables=soup.find_all("table")
	h3s = soup.find_all("h3")
	i=0 
	for table in tables:
		rtn += ("### %s\n" %(h3s[i].get_text()))
		i+=1

		theTRs = table.find_all("tr")
		for tr in theTRs:
			temp =""
			cols = tr.findAll('td')
			if len(cols) == 2:
				temp += cols[0].get_text()
				temp += " "
				temp += cols[1].get_text()
			if len(cols) == 3:
				temp += cols[0].get_text()
				temp += ": "
				temp += cols[1].get_text()
			if len(temp.strip()) >0:
				rtn += (("* %s\n" %(temp)))

	return rtn
# def get_html_ip(ip):
# 	url = ("http://www.ipvoid.com/scan/%s/" %(ip))
# 	values = {'url' : ip, 'go':'Scan Now'}

# 	data = urllib.urlencode(values)
# 	req = urllib2.Request(url, data)
# 	response = urllib2.urlopen(req)
# 	html = response.read()
# 	return html
def get_html_ip(ip):
	html = urllib2.urlopen(("http://www.ipvoid.com/scan/%s/" %(ip))).read()
	return html
def get_info(inquery):
	if inquery.__class__.__name__ == 'IP':
		html = get_html_ip(inquery.address)
		rtn = get_elements(html)
		return rtn
	if inquery.__class__.__name__ == 'URL':
		rtn = get_html_url(inquery.address)
		return rtn
def get_html_url(url):
	rtn = """
	IP Void does not let you query urls.
	"""
	return rtn