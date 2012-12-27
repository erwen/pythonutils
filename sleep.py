#!/bin/env python

#Author:finalbsd@gmail.com
#Date: 2012-12-25

import time
import getopt
import sys


def usage():
	print '''
Usage: sleep NUMBER[SUFFIX]...
  or:  sleep OPTION
Pause for NUMBER seconds.  SUFFIX may be `s' for seconds (the default),
`m' for minutes, `h' for hours or `d' for days.  Unlike most implementations
that require NUMBER be an integer, here NUMBER may be an arbitrary floating
point number.  Given two or more arguments, pause for the amount of time
specified by the sum of their values.

      --help     display this help and exit
      --version  output version information and exit

Report sleep bugs to bug-coreutils@gnu.org
GNU coreutils home page: <http://www.gnu.org/software/coreutils/>
General help using GNU software: <http://www.gnu.org/gethelp/>
Report sleep translation bugs to <http://translationproject.org/team/>
For complete documentation, run: info coreutils 'sleep invocation'
'''
	sys.exit(0)

def version():
	print '''
sleep (GNU coreutils) 8.4
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jim Meyering and Paul Eggert.
'''
	sys.exit(0)


try:
	opts, args = getopt.getopt(sys.argv[1:],'hv',['version','help'])
except getopt.GetoptError as err:
	print("Getopt Error:" + str(err))

for opt, arg in opts:
	if opt in ['-h','--help']:
		usage()
	if opt in ['-v','--version']:
		version()
i = 0
while i < len(args):
	if 's' in args[i]:
		args[i] = float(args[i][:-1])
	elif 'm' in args[i]:
		args[i] = float(args[i][:-1]) * 60
	elif 'h' in args[i]:
		args[i] = float(args[i][:-1]) * 60 * 60 
	elif 'd' in  args[i]:
		args[i] = float(args[i][:-1]) * 60 * 60 * 24
	else:
		args[i] = float(args[i])
	i+=1

time.sleep(sum(args))
