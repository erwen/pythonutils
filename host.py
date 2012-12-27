#!/bin/env python3

import sys
import socket
import getopt

def hostname(name=None):
	if name is None:
		name = socket.gethostname()
		return name
	else:
		socket.sethostname(name)
		pass

def usage():
	print('''Usage: hostname [-fs] [name-of-host]
     The hostname utility prints the name of the current host.  The super-user
     can set the hostname by supplying an argument; this is usually done in
     the initialization script /etc/rc.d/rc.sysinit, normally run at boot time.
     
	 Options:
     
	 -f    Include domain information in the printed name.  This is the
           default behavior.

     -s --short   Trim off any domain information from the printed name.
     -h --help    Show this help.
     -v --version Show the version.  ''')


VERSION = '1.0.0'

try:
	opts, args = getopt.getopt(sys.argv[1:], 'fsvh', ['short', 'version', 'help'])
except getopt.GetoptError as err:
	print('hostname: %s, try hostname -h for a list of all the options' % str(err))
	usage()
	sys.exit(2)


if args:
	hostname(args[0])
	sys.exit(0)
elif opts:
	for opt, arg in opts:
		if opt in ['-v', '--version']:
			print("Version: " + VERSION)
		if opt in ['-f']:
			print(hostname())	
		if opt in ['-s', '--short']:
			print(hostname().split('.')[0])
		if opt in ['-h', '--help']:
			usage()
else:
	print(hostname())
