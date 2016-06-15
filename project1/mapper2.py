#!/usr/bin/env python
import sys

for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) == 6:
			# print store store and sale
			print '%s\t%s' % (data[2], data[4])