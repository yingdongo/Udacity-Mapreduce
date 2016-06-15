#!/usr/bin/env python

import sys
import re
# match the request line from the client
pattern = '"(.*?)\ (.*?)\ (.*?)"'

for line in sys.stdin:
	result = re.search(pattern, line.strip())
	if result:
		# second group is the path
		path = result.group(2)
		# remove http://www.the-associates.co.uk
		path = path.replace("http://www.the-associates.co.uk", "")
		print "%s\t%s" % (path, 1)