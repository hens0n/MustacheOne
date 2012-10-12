#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup

def GetDomainInfo(Domain):
	#PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.intodns.com/'+Domain).read())