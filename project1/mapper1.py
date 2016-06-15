#!/usr/bin/env python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) == 6:
		date, time, name, product, sale, pay = data
		print '%s\t%s' % (product, sale)
