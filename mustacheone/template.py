#!/usr/bin/python
# -*- coding: latin-1 -*-

def get_header():
	rtn = """
###Source
[Source Website](https://www.foo.com)

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