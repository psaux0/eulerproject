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
def phi(n):
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

x=0
for i in xrange(1,1000001):
	x+=phi(i)
print x-1


"""
As most people, I saw that for each denominator n there are Phi(n) proper fractions. So the final answer is Phi(2) + Phi(3) + ... + Phi(1000000). As for dynamically generating Phi(n), we know that Phi(n) = n-1 if n is prime. In all other cases, we have to split n in two coprime factors. I do this by finding the smallest prime p that divides n and then taking the highest power pow of that prime that still divides n. Then Phi(n) = Phi(p)*(pow/p)*Phi(n/pow). Takes 1.5s incl. prime generation by sieve.:
"""

for n in range(2,1000001):
    if n in primeSet:
        totients.append(n-1)
    else:
        for prime in primes:
            if n%prime == 0:
                power = prime
                while n%(power*prime) == 0:
                    power *= prime
                totients.append(totients[prime]*(power/prime)*totients[n/power])
                break
print sum(totients[2:])