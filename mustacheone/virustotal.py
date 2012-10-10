#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 
import simplejson
import urllib
import urllib2

def PrintHeader():
	header ="""         
 _   _ _              _____     _         _ 
| | | (_)            |_   _|   | |       | |
| | | |_ _ __ _   _ ___| | ___ | |_  __ _| |
| | | | | '__| | | / __| |/ _ \| __|/ _` | |
\ \_/ / | |  | |_| \__ \ | (_) | |_| (_| | |
 \___/|_|_|   \__,_|___|_/\___/ \__|\__,_|_|
	https://www.virustotal.com
	"""
	print(header)

def ScanURL(url):
	parameters = {"url": url, "apikey": "yourAPIkey"}
	data = urllib.urlencode(parameters)
	req = urllib2.Request("https://www.virustotal.com/vtapi/v2/url/scan", data)
	response = urllib2.urlopen(req)
	theJson = response.read()
	#print(theJson)

def GetUrlReport(url):
	PrintHeader()
	parameters = {"resource": url, "apikey": "yourAPIkey"}
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
		ScanURL(url)
		print("Scan not complete, Summiting Scan to VirusTotal")	