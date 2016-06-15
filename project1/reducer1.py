#!/usr/bin/env python

import sys

current_key = None
current_sale = 0

for line in sys.stdin:

	data = line.strip().split('\t')
	key, sale = data

	if current_key and current_key != key:
		print '%s\t%s' % (current_key, current_sale)
		current_sale = 0

	current_key = key
	current_sale += float(sale)
print '%s\t%s' % (current_key, current_sale)
