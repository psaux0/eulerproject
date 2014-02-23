def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]

def isEndWith(n):
	if (str(n)[-1] == '3' or str(n)[-1] == '7') and (str(n)[0] == '3' or str(n)[0] == '7' or str(n)[0]=='2' or str(n)[0]=='5'):
		return True
	else :
		return False


l=primes(800000)

def truncatable(n):
	w=str(n)
	for i in xrange(1,len(w)-1):
		if not ((int(w[i:]) in l) and (int(w[:len(w)-i]) in l)):
			return False
	return True


k=filter(isEndWith,l)
u=filter(truncatable,k)

print sum(u)-10



#a better solution
def numberOfDigits(n):
   from math import log
   return int(log(n,10)) + 1

def rightTruncates(q):
   ''' rightTruncates(int) -> iterator  yield all the right truncates of a number, e.g. 123 returns 23, 3
   but 101 returns only 1'''
   while q > 9:
      # need to recompute the number of digits in case on contained 0
      q %= 10**(numberOfDigits(q)-1)
      yield q

def leftTruncates(q):
   '''leftTruncates(int) -> iterator -- Yields all the left truncates of a number'''
   while q > 9:
      q //= 10
      yield q

def isMadeOfOddOrWithLeading2(n):
   '''isMadeOfOddOrWithLeading2(int) -> bool -- Checks if a number is made of the form abcd with b,c,d odd numbers and a odd number or 2'''
   while n > 10:
      if not n % 10 in {1,3,7,9}: return False
      n //= 10
   return n % 10 in {1,2,3,5,7,9}

def iPrime( ):
   from itertools import count
   '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
   D = {  }  # map each composite integer to its first-found prime factor
   # To speed things up, we deal with 2 as a special case
   yield 2
   for q in count(3,2):     # q gets 3, 5, 7, ... ad infinitum
      p = D.pop(q, None)
      if p is None:
         # q not a key in D, so q is prime, therefore, yield it
         yield q
         # mark q squared as not-prime (with q as first-found prime factor)
         D[q*q] = q
      else:
         # let x <- smallest (N*p)+q which wasn't yet known to be composite
         # we just learned x is composite, with p first-found prime factor,
         # since p is the first-found prime factor of q -- find and mark it
         x = p + q
         while x in D or x % 2 == 0:
            x += p
         D[x] = p

def problem37():
   found = set()
   primes = iPrime()
   # The primes 2,3,5,7 are not candinates, but they could be the result of a truncation.
   primesOfInterest = {next(primes),next(primes),next(primes),next(primes)}
   for q in primes:
      if isMadeOfOddOrWithLeading2(q):
         primesOfInterest.add(q)
         if all(p in primesOfInterest for p in leftTruncates(q)) and all(p in primesOfInterest for p in rightTruncates(q)):
            found.add(q)
            if len(found) > 10:
               return sum(found)

import cProfile
if __name__ == "__main__":
   print(problem37() == 748317)
   cProfile.run("problem37()")
