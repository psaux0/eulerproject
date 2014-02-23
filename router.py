#!/usr/bin/env python2

def fac(num):
    if num==1:
        return 1
    else :
        return num*fac(num-1)

multi=1
for i in xrange(21,41):
    multi*=i

print multi/fac(20)
