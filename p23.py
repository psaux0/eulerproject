from time import time
t1=time()
def factors(n):
	i=1
	while i*i<=n:
		if not n%i:
			yield i
			yield n//i
		i+=1
	if i*i==n:
		yield i

def isAbundant(n):
	return sum(set(factors(n)))>2*n

b=list()
for i in xrange(28124):
	if isAbundant(i):
		b.append(i)


w=list()
for i in xrange(len(b)):
	for j in xrange(i,len(b)):
		tmp=b[i]+b[j]
		if tmp>28123:
			break          #break only breaks one loop, so does continue
		w.append(tmp)


print sum(set(range(28123))-set(w)),time()-t1


#a better solution which needs a lot of math

def d(n):
   ''' A fast version of sigma(n,1), does not work for large n'''
   # We already acount for the trivial divisors 1
   sigma = 1
   # We only need to check for divisors up to √n
   m  = n ** 1/2
   # If n is a square, we are over overcounting it
   if m == int(m): sigma -= int(m)
   m = int(m) + 1
   for i in range(2, m):
      # For every divisor, we get a pair of divisors
      if n % i == 0: sigma += i + n//i
   return sigma

def problem23():
   # The first few numbers are easily cases
   abundantNumbers = {12,18,20}
   total = 24*(23)/2 + 20161
   # http://mathworld.wolfram.com/AbundantNumber.html
   # Every number greater than 20161 can be expressed as a sum of two abundant numbers
   for n in range(24,20161):
      # only numbers divisible by 2 or 3 are abundant for small numbers
      # A number that is divisible by 6 is abundant
      if not (n%6 in {1,5}) and (n%6 == 0 or d(n) > n):
         abundantNumbers.add(n)
      if not any( n-j in abundantNumbers for j in abundantNumbers): total += n
   return total