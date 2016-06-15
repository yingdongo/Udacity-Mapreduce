#!/usr/bin/env python

# Find the monetary value for the highest individual sale for each separate store.

import sys

current_store = None
current_sale = 0

for line in sys.stdin:
	store, sale = line.strip().split("\t")

	if current_store == None:
		current_store = store
		current_sale = sale

	elif current_store != store:
		print '%s\t%s' % (current_store, current_sale) 
		current_store = store
		current_sale = sale

	if float(sale) > float(current_sale):
		current_sale = sale

print '%s\t%s' % (current_store, current_sale) 
 
