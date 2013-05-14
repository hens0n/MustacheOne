#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import ConfigParser
import mustacheone



def main(argv):
	report = ""
	if len(argv)==0:
		print mustacheone.usage()
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