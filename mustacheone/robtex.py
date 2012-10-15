#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import urllib2

from bs4 import BeautifulSoup

def GetIpInfo(IP):
	PrintHeader()
	soup = BeautifulSoup(urllib2.urlopen('http://www.robtex.com/ip/'+IP+'.html').read())
	ParseListFromRobtex("sharedha","Host names sharing IP with A records",soup)
	ParseListFromRobtex("sharedal","IP numbers of host",soup)
	ParseListFromRobtex("sharedaptra","A of PTR of A",soup)
	ParseListFromRobtex("sharedmxa","Domains using this as mail server under another name",soup)
	ParseListFromRobtex("sharedpal","PTRs of IP numbers",soup)

def ParseListFromRobtex(tag_id,description, theSoup):
	print(description)
	theTag =theSoup.find(id=tag_id)
	if theTag != None:
		li_tag =theTag.parent.next_sibling
		if li_tag != None:	
			for child in li_tag:
				print("    "+child.contents[0].string.encode('ascii', 'ignore'))
		else:
			print("none")
	else:
		print("none")


def PrintHeader():
	header ="""
************************
RobTex
http://www.robtex.com
************************
"""
	print(header)
