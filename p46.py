import time
t1=time.time()
def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]

def goldBach(n):
	p=primes(n+1)
	for i in p:
		k=(n-i)/2
		if k**0.5 == int(k**0.5):
			return True
	return False

k=37
while goldBach(k):
	k+=2

t2=time.time()
print k,t2-t1

#a better solution
