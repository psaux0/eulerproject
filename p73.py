import time
t1=time.time()

#generate prime factors of a number
def primeFactors(n):
	i=2
	while i*i<=n:
		while not n%i:
			yield i
			n//=i
		i+=1
	if n>1:
		yield n
		
#sieve out the times of prime factors and compute the number between n/2,n/3
def specialPhi(n):
	p=[0]*(n/2+1)
	for i in set(primeFactors(n)):
		p[i::i]=[1]*((n-2*i+1)/(2*i)+1)
	return len([i for i in xrange(n/3+1,n/2+1) if not p[i]])

count=0
for i in xrange(5,12001):
	count+=specialPhi(i)

t2=time.time()
print count,t2-t1

#another way, put here to record
import math
start_time = time.clock()
print

target = 10**6

def phi_sum(limit):
   phi = range(limit + 1)
   for n in xrange(2, limit + 1):
      if phi[n] == n:
         for k in xrange(n, limit + 1, n):
            phi[k] = phi[k] / n * (n-1)
   return sum(phi) - 1
   
      
print phi_sum(target)
   
      
print
print time.clock() - start_time
print