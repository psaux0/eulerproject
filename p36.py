from time import time
t=time()

def dtobCompare(n):
	binaryList=list()
	while n>0:
		binaryList.append(n%2)
		n/=2
	tmp=binaryList[:]
	binaryList.reverse()
	return tmp == binaryList

def dCompare(n):
	s=str(n)
	return s == ''.join([x for x in reversed(s)])

l=list()

for i in xrange(1,1000001):
	if dCompare(i) and dtobCompare(i):
		l.append(i)


k=sum(l)

t2=time()
print k,t2-t
#actually python has built-in function bin which can be used to make binary

