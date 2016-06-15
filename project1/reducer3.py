#!/usr/bin/env python

# find total number of sales and total sales value from all stores
import sys

total_sale = 0
total_num = 0

for line in sys.stdin:
	sale = line.strip()
	sale = float(sale)
	
	total_sale += sale
	total_num += 1

print '%s\t%s' % (total_sale, total_num) 
 
