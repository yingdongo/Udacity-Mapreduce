#!/usr/bin/env python

# hits prt IP
import sys

current_key = None
current_value = 0

for line in sys.stdin:

	data = line.strip().split('\t')
	key, value = data

	if current_key and current_key != key:
		print '%s\t%s' % (current_key, current_value)
		current_value = 0

	current_key = key
	current_value += int(value)
print '%s\t%s' % (current_key, current_value)
