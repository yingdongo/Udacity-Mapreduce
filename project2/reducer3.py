#!/usr/bin/env python

# find the most frequent path
import sys

current_path = None
current_hits = 0
max_hits = 0
max_path = None
for line in sys.stdin:
	path, hits = line.split("\t")
	hits = int(hits)
	if current_path == None:
		current_path = path

	if current_path != path:
		if current_hits > max_hits:
			max_hits = current_hits
			max_path = current_path

		current_path = path
		current_hits = 0

	current_hits += hits

if current_hits > max_hits:
	max_hits = current_hits
	max_path = current_path

print "%s\t%s" % (max_path, max_hits)


