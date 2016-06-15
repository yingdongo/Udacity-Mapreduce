#!/usr/bin/env python

import sys
import re

pattern = '"(.*?)\ (.*?)\ (.*?)"'

for line in sys.stdin:
	result = re.search(pattern, line.strip())
	try:
		print "%s\t%s" % (result.group(2), 1)
	except ValueError:
		raise
