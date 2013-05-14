#!/usr/bin/python
# -*- coding: latin-1 -*-

def get_header():
	rtn = """
Google Recon Queries
--------------------
[Google Website](http://www.google.com)

"""
	return rtn

def get_info(inquery):
	if inquery.__class__.__name__ == 'IP':
		return get_html_ip(inquery.address)
	if inquery.__class__.__name__ == 'URL':
		return get_html_url(inquery.address)
def get_html_ip(ip):
	rtn = """
	Not Complete

	"""
	return rtn
def get_html_url(url):
	rtn = ("- [Subdomains excluding www: site:%s -www. %s](http://www.google.com/?q=site:%s -www. %s)\n" % (url,url,url,url))
	rtn += ("- [Office files from %s: filetype:xlsx OR filetype:pptx OR filetype:docx site:%s](http://www.google.com/?q=filetype:xlsx OR filetype:pptx OR filetype:docx site:%s)\n" % (url,url,url))
	rtn += ("- [Subdomains excluding www: site:%s -www. %s](http://www.google.com/?q=site:%s -www. %s)\n" % (url,url,url,url))
	rtn += ("- [PDF files from %s: filetype:pdf site:%s](http://www.google.com/?q=filetype:pdf site:%s)\n" % (url,url,url))
	rtn += ("- [Links to %s: link:%s](http://www.google.com/?q=link:%s)\n" % (url,url,url))
	rtn += ("- [Email Addresses: @%s -www.%s](http://www.google.com/?q=Email Addresses: @%s -www.%s)\n" % (url,url,url,url))

	return rtn