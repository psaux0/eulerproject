import time
t1=time.time()
def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]


p=primes(1000000)
q=[0]*len(p)

total=0
for i in xrange(len(p)):
	total+=p[i]
	q[i]=total

longest=0
w=0
for x in xrange(1,len(p)):
	for j in xrange(x-longest-1,-1,-1):
		tmp=q[x]-q[j]
		if tmp>1000000:
			break
		if tmp in p:
			longest=x-j
			w=tmp
t2=time.time()
print longest,w,t2-t1
