import time
t1=time.time()
def T(n):
	for i in xrange(1,n+1):
		yield (i+1)*i/2

def P(n):
	for i in xrange(1,n+1):
		yield (3*i-1)*i/2

def H(n):
	for i in xrange(1,n+1):
		yield (2*i-1)*i

s=set(T(100000)) & set(P(100000)) & set(H(100000))

t2=time.time()
print s ,t2-t1