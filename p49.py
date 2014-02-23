import time
t1=time.time()
def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]

largePrimes=filter(lambda x:x>1000,primes(10000))

a=[[0]]*len(largePrimes)

for i in xrange(len(largePrimes)):
	if largePrimes[i]==1:
		continue
	if a[i]==[0]:
		a[i]=[largePrimes[i]]
	for j in xrange(i+1,len(largePrimes)):
		if sorted([x for x in str(largePrimes[i])]) == sorted([x for x in str(largePrimes[j])]):
			a[i].append(largePrimes[j])
			largePrimes[j]=1

d=[i for i in a if len(i)>2]

def arith(arr):
	for i in xrange(len(arr)-2):
		for j in xrange(i+2,len(arr)):
			if (arr[i]+arr[j])/2 in arr:
				return arr[i],(arr[i]+arr[j])/2,arr[j]
	return False

for j in d:
	if arith(j):
		print arith(j)

t2=time.time()
print t2-t1
