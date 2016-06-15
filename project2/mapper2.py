#!/usr/bin/env python

import sys
import re

# match IP address from request string
pattern = "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*"

for line in sys.stdin:
	result = re.search(pattern, line.strip())
	if result:
		print "%s\t%s" % (result.group(), 1)
