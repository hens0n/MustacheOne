#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2

sys.path.append('libs/')
from bs4 import BeautifulSoup

def get_header():
	rtn = """
Project Honey Pot
-----------------
[Project Honey Pot Website](http://www.projecthoneypot.org)

"""
	return rtn

def get_info(inquery):
	if inquery.__class__.__name__ == 'IP':
		return get_html_ip(inquery.address)
	if inquery.__class__.__name__ == 'URL':
		return get_html_url(inquery.address)
def get_html_ip(ip):
	soup = BeautifulSoup(urllib2.urlopen('http://www.projecthoneypot.org/ip_'+ip).read())
	theTag =soup.find("div", { "class" : "contain" })
	rtn = theTag.contents[3].get_text().encode('ascii', 'ignore').strip() + "\n"
	return rtn
def get_html_url(url):
	rtn = """
	Project Honey Pot does not let you query urls.

	"""
	return rtn