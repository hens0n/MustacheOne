#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys 

def PrintHeader():
	header ="""         
************************
Google
http://www.google.com
************************
	"""
	print(header)

def PrintQueries(Domain):
	PrintHeader()

	print("Google queries to help with recon")
	print("\t* Subdomains excluding www: site:domain.com -www."+Domain)
	print("\t* Office files from "+Domain+": filetype:xlsx OR filetype:pptx OR filetype:docx site:"+Domain)
	print("\t* PDF files from "+Domain+": filetype:pdf site:"+Domain)
	print("\t* Links to "+Domain+": link:"+Domain)
	print("\t* Email Addresses: \"@"+Domain+"\" -www."+Domain)