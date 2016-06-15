#!/usr/bin/env python
import sys

for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) == 6:
			# print sale value
			print '%s\t' % (data[4])