#!/usr/bin/env python

#Find the total sales value of every store, and the total number of sales of every store

import sys

current_store = None
current_sale = 0
current_num = 0

for line in sys.stdin:
	store, sale = line.strip().split("\t")
	sale = float(sale)
	if current_store == None:
		current_store = store
		current_sale = sale

	elif current_store != store:
		print '%s\t%s\t%s' % (current_store, current_sale, current_num) 
		current_store = store
		current_sale = sale
		current_num = 0

	current_sale += sale
	current_num += 1

print '%s\t%s\t%s' % (current_store, current_sale, current_num) 
 
