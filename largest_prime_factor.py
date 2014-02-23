#!/usr/bin/env python2

def primes(n):
    s = xrange(3,n,2)
    mroot=n**0.5
    half=len(s)
    i=0
    m=3
    while m<=mroot:
        if s[i]:
            j=(m*m-3)//2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [x for x in s if x]

io=600851475143
iou=io/3
x=primes(iou)

for i in x.reverse():
    if i%io == 0:
        print i
        break
