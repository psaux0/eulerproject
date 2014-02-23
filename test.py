from time import time
t1=time()
#a special kind of multiplay
def newMulti(a,b):
	if a*b<10000000000:
		c=a*b
	else:
		c=a*b-a*b/10000000000*10000000000
	return c

def newPow(n,j):
	k=1
	for x in xrange(j):
		k=newMulti(k,n)
	return k 

def newAdd(a,b):
	if a+b<10000000000:
		c=a+b
	else:
		c=a+b-(a+b)/10000000000*10000000000
	return c

sumNew=0
for i in xrange(1,1000):
	sumNew=newAdd(sumNew,newPow(i,i))
print sumNew

t2=time()
print t2-t1