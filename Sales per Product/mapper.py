#!/usr/bin/env python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if len(data) ==6:
        date, time, name, product, sales, pay = data
        print '%s\t%s' % (product, sales)
