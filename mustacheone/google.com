#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib
import urllib2

from bs4 import BeautifulSoup

def GetDomainInfo(Domain):
	#PrintHeader()
	#soup = BeautifulSoup(urllib2.urlopen('http://uptime.netcraft.com/up/graph/?host='+Domain).read())
	#site:domain.com -www.domain.com
	#filetype:xlsx OR filetype:pptx OR filetype:docx site:www.domain.com
	#link:www.domain.com
	#"@domain.com" -www.domain.com