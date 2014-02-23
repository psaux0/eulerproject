def primefactors(n):
	i=2
	while i*i<=n:
		while not n%i:
			yield i
			n//=i
		i+=1
	if n>1:
		yield n
#a really fast way to compute phi, more in numbthy.py
def phi3(n):
	thefactors=sorted(list(primefactors(n)))
	phi=1
	oldfact=1
	for fact in thefactors:
		if fact==oldfact:
			phi=phi*fact
		else:
			phi=phi*(fact-1)
			oldfact=fact
	return phi

def isPermutation(a,b):
	return sorted(str(a))==sorted(str(b))

m=10
k=0
for n in xrange(7*10**6+1,9*10**6,2):
	ee=phi3(n)
	if not isPermutation(n,ee):
		continue
	r=n*1.0/ee
	if r<m:
		m=r
		k=n
print m,k,phi3(k)


#using math to solve problem
def isPermutation(n1, n2):
        return sorted(list(str(n1))) == sorted(list(str(n2)))

def getPrimesSieve(limit):
        notPrimes = [False] * limit
        primes = []
        for i in range(2, limit):
                if notPrimes[i]:
                        continue
                for f in xrange(i*2, limit, i):
                        notPrimes[f] = True
                primes.append(i)
        return primes

bestN, minRatio = 0, 2.0
primes = filter(lambda n: n > 2000, getPrimesSieve(5000))
for i in xrange(len(primes)):
        for j in xrange(i+1, len(primes)):
                n = primes[i] * primes[j];
                if n > 10000000:
                        break
                phiN = (primes[i] - 1) * (primes[j] - 1)
                if isPermutation(n, phiN):
                        ratio = float(n) / phiN
                        if ratio < minRatio:
                                bestN, minRatio = n, ratio
print bestN, phiN, minRatio

"""
Python, runs in 150 ms. Based off of the knowledge that n cannot be prime (because phi(n) could not be permutation), 
and to minimize n/phi(n) we need an n that is the product of two larger primes. 
"""