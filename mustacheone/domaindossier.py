#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup

def GetIpInfoPost(IP):
	#PrintHeader()
	url = BeautifulSoup(urllib2.urlopen('http://centralops.net/co/DomainDossier.aspx?dom_whois=true&dom_dns=true&traceroute=true&net_whois=true&svc_scan=true&x=15&y=11&addr=github.com').read())


	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()

	soup = BeautifulSoup(the_page)
	print(soup)
