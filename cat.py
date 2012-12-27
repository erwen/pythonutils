#!/bin/env python

from __future__ import print_function
import getopt
import sys
import math

try:
	opts, args = getopt.getopt(sys.argv[1:], 'nA')
except getopt.GetoptError as err:
	print("Error: " + str(err))
	sys.exit(2)



def cook_cat(flist,lineno=False,showall=False):
	for file in flist: 
		try:
			with open(file) as out:
				i = 1
				for each_line in out:
					if showall:
						if each_line.find('\n'):
							line = each_line.replace('\n','$')
						elif each_line.find('\t'):
							line = each_line.replace('\t','^I')
					if lineno:
						print('%(number)6d %(line)s' %{'number':i,'line' :line})
						i += 1
					else:
						print(line)
		except IOError as ioerr:
			print("IOError: " + str(ioerr))
for opt, arg in opts:
	if opt in '-n':
		cook_cat(args, lineno=True)
		sys.exit(0)
	if opt in '-A':
		cook_cat(args, showall=True)
