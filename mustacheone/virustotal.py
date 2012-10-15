#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import simplejson
import urllib
import urllib2

def PrintHeader():
	header ="""  
************************       
VirusTotal
https://www.virustotal.com
************************ 
	"""
	print(header)

def ScanURL(url,apikey):
	parameters = {"url": url, "apikey": apikey}
	data = urllib.urlencode(parameters)
	req = urllib2.Request("https://www.virustotal.com/vtapi/v2/url/scan", data)
	response = urllib2.urlopen(req)
	theJson = response.read()
	#print(theJson)

def GetUrlReport(url,apikey):
	PrintHeader()
	parameters = {"resource": url, "apikey": apikey}
	data = urllib.urlencode(parameters)
	req = urllib2.Request("https://www.virustotal.com/vtapi/v2/url/report", data)
	response = urllib2.urlopen(req)

	theJson = response.read()
	if theJson.find("permalink") > -1:
		sjson = simplejson.loads(theJson)
		scans = sjson['scans']
		if scans != None:
			for o in scans:
				print(o +": " + scans[o]['result'])	
	else:
		ScanURL(url,apikey)
		print("Scan not complete, Summiting Scan to VirusTotal")	