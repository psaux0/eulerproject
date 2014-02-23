def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]

p=primes(10**7)

def isPermutation(a,b):
	return sorted(str(a))==sorted(str(b))

for i in p:
	if isPermutation(i,i-1):
		print i 
