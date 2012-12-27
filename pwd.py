#!/bin/env python

# Kevin@2012/12/26

import os
import sys
import getopt

VERSION='1.0.0'

def usage():
	print("pwd: usage: pwd [-LP]")
	sys.exit(0)
def print_version():
	print("pwd version:" + VERSION)
	sys.exit(0)

try:
	opts, args = getopt.getopt(sys.argv[1:],'LP',['help', 'version'])
except getopt.GetoptError as error:
	print("getopt error:" + str(error))

if not opts:
	print(os.getenv("PWD"))
else:
	for opt, arg in opts:
			if opt in ['-L','--logical']:
				print(os.getenv("PWD"))
			if opt in ['-P','--physical']:
				print(os.getcwd())
			if opt in ['--help']:
				usage()
			if opt in ['--version']:
				print_version()
