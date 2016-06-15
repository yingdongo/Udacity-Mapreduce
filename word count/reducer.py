#!/usr/bin/env python

import sys

current_key = None
current_sales = 0

for line in sys.stdin:

	data = line.strip().split('\t')
	key, sales = data

	if current_key and current_key != key:
		print '%s\t%s' % (current_key, current_sales)
		current_sales = 0

	current_key = key
	current_sales += float(sales)

print '%s\t%s' % (current_key, current_sales)
