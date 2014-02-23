#!/usr/bin/env python2

def fab(max):
    n,a,b = 0,1,2
    while n < max:
        yield b
        a,b = b,a+b
        n=n+1

max=20
while True:
    if tuple(fab(max))[max-1] > 4000000 :
        print max
        break

sumFab=0
for i in fab(max-1):
    if i/2*2==i:
        sumFab=sumFab+i
print sumFab




