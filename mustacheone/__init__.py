#!/usr/bin/python
# -*- coding: latin-1 -*-
import datetime
import sys
import socket
import string

import projecthoneypot
import google
import intodns
import ipvoid

sys.path.append('libs/')
import cherrypy
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
import markdown

def usage():
	rtn = """
	* Please provide an argument(s)
	* Single URL usage: MustacheOne.py github.com
	* Single IP usage: MustacheOne.py 208.78.70.16
	* Combination usage: MustacheOne.py github.com 208.78.70.16 google.com
	* Launch WebGUI(Open 127.0.0.1:8080): MustacheOne.py webgui
	"""
	return rtn

def get_header(query):
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	header ="""
MustacheOne
===========                                                        
[MustacheOne Source on GitHub](https://github.com/cyberphilia/MustacheOne)

"""
	header += ("Report generated on %s" %(now))
	header += (" for %s\r\n" %(query))
	return header
def get_report(query):
	if is_ip(query):
		ip = IP()
		ip.address = query
		report = get_reports(ip)
	else:
		url = URL()
		url.address = query
		report = get_reports(url)

	

	return report
def get_reports(parm):
	report = ""
	report += get_header(parm.address)
	report += projecthoneypot.get_header()
	report += projecthoneypot.get_info(parm)
	report += intodns.get_header()
	report += intodns.get_info(parm)
	report += ipvoid.get_header()
	report += ipvoid.get_info(parm)
	report += google.get_header()
	report += google.get_info(parm)
	return report

def is_ip(query):
	try:
		socket.inet_aton(query)
		return True
	except socket.error:
		return False

def get_config(section, name):
	try:
		config = ConfigParser.RawConfigParser()
		config.read('config.ini')
		rtn = config.get(section,name)
		return rtn
	except ConfigParser.NoSectionError:
		print("Section Not Found")
	except ConfigParser.NoOptionError:
		print("Option Not Found")

class IP:
	address = ''
class URL:
	address = ''
def start_webgui():
	cherrypy.quickstart(webgui())
class webgui:
	@cherrypy.expose
	def index(self):
		mytemplate = Template(filename='mustacheone/base.html')
		return mytemplate.render(inquery='')
	@cherrypy.expose
	def search(self, inquery=None):
		mytemplate = Template(filename='mustacheone/base.html')
		reports = ''
		lines = string.split(inquery, '\n')
		for line in lines:
			reports += get_report(line) + '\n***'
		# reports = get_report('69.147.143.2')
		# reports = get_report('camber.com')
		if len(reports) >0 :
			return mytemplate.render(inquery=inquery, reports=markdown.markdown(reports))
		else:
			return mytemplate.render(inquery=inquery)