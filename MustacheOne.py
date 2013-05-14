#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import ConfigParser
import mustacheone



def main(argv):
	report = ""
	if len(argv)==0:
		print mustacheone.usage()

		report = mustacheone.get_report('google.com')
		# report = mustacheone.get_report('63.233.126.124')
		# foo = mustacheone.URL()
		# foo.address = 'camber.com'
		# report += mustacheone.get_header(foo.address)

		#print 
		print report

	else:
		for arg in argv:
			if arg == 'webgui':
				print 'webgui'
				mustacheone.start_webgui()
			else:
				report = mustacheone.get_report(arg)
				print report

if __name__ == "__main__":
	main(sys.argv[1:])