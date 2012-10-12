#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup

def GetDomainInfo(Domain):
	#PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://uptime.netcraft.com/up/graph/?host='+Domain).read())
	#'http://toolbar.netcraft.com/site_report?url='+Domain