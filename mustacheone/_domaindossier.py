#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup
def PrintHeader():
	header ="""  
************************       
DomainDossier
http://centralops.net/co/DomainDossier.aspx
************************ 
	"""
	print(header)
def GetIpInfo(IP):
	#PrintHeader()
	try:
		soup = BeautifulSoup(urllib2.urlopen('http://centralops.net/co/DomainDossier.aspx?dom_whois=true&dom_dns=true&traceroute=true&net_whois=true&svc_scan=true&x=15&y=11&addr='+IP).read())
		print(soup)
	except urllib2.HTTPError:
		print("HTTP Error")
	