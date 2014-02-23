import time
from collections import deque

time1=time.time()
def allCircular(n):
	numberList=deque([int(i) for i in str(n)])
	l=list()
	k=0
	while k<len(numberList):
		l.append(makeInt(numberList))
		numberList.rotate(1)
		k+=1
	return set(l)

def makeInt(q):
	k=0
	for i in xrange(len(q)):
		k=k+q[i]*10**(len(q)-i-1)
	return k

def Primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]


lj=Primes(1000000)
primeList=set(lj)
count=0
for i in lj:
	p=allCircular(i)
	if primeList.intersection(p)==p:
		count+=1

time2=time.time()
print count,time2-time1

