#!/usr/bin/python
# -*- coding: latin-1 -*-

def get_header():
	rtn = """
###VirusTotal
[VirusTotal Website](https://www.virustotal.com)

"""
	return rtn

def get_info(inquery):
	if inquery.__class__.__name__ == 'IP':
		return get_html_ip(inquery.address)
	if inquery.__class__.__name__ == 'URL':
		return get_html_url(inquery.address)
def get_html_ip(ip):
	rtn = "Not Implemented"
	return rtn
def get_html_url(url):
	rtn = "Not Implemented"

	return rtn

	
# def GetUrlReport(url,apikey):
# 	PrintHeader()
# 	parameters = {"resource": url, "apikey": apikey}
# 	data = urllib.urlencode(parameters)
# 	req = urllib2.Request("https://www.virustotal.com/vtapi/v2/url/report", data)
# 	response = urllib2.urlopen(req)

# 	theJson = response.read()
# 	if theJson.find("permalink") > -1:
# 		sjson = simplejson.loads(theJson)
# 		scans = sjson['scans']
# 		if scans != None:
# 			for o in scans:
# 				print(o +": " + scans[o]['result'])	
# 	else:
# 		ScanURL(url,apikey)
# 		print("Scan not complete, Summiting Scan to VirusTotal")	
# def ScanURL(url,apikey):
# 	parameters = {"url": url, "apikey": apikey}
# 	data = urllib.urlencode(parameters)
# 	req = urllib2.Request("https://www.virustotal.com/vtapi/v2/url/scan", data)
# 	response = urllib2.urlopen(req)
# 	theJson = response.read()