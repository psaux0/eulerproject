#!/usr/python/env python2

import time

time1=time.time()

for c in xrange(333,500):
    x=1000-c
    for b in xrange(c/2,c):
        if b**2+(x-b)**2==c**2:
            print b*c*(1000-b-c)
            break

time2=time.time()

print time2-time1
