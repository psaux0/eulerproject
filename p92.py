happyNumbers=[1,10,100,1000,10000,100000,1000000,10000000]
unhappyNumbers=[89]

def digitSquare(n):
	x=digitSquareSum(n)
	while (not (x in happyNumbers)) and (not (x in unhappyNumbers)):
		yield x
		x=digitSquareSum(x)
	yield x


def digitSquareSum(n):
	return sum([int(i)**2 for i in str(n)])

count=0
for i in xrange(1,10000000):
	if i in happyNumbers:
		count+=1
		continue
	n=tuple(digitSquare(i))
	if n[-1] in happyNumbers:
		count+=1
		happyNumbers.extend(n[:-1])
	else:
		unhappyNumbers.extend(n[:-1])

print 10*7-count-1

	
#an easier way but faster way
#!/usr/bin/env python
from functools import reduce

def memoize(obj):
    cache = {}
 
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

@memoize
def chain(n):
    if n == 1 or n == 89:
        return n
    else:
        return chain(sum(map(lambda el: int(el)**2, str(n))))

def euler92():
    return reduce(lambda x,_: x+1, filter(lambda n: chain(n) == 89, range(1,10000000)),0)

if __name__ == "__main__":
    print(euler92())
"""
def isHappyNumber(n):
	cache=[]
	if n in happyNumbers:
		return True
	elif n in unhappyNumbers:
		return False
	else:
		x=digitSquareSum(n)
		cache.append(n)
		while True:
			cache.append(x)
			if x in happyNumbers:
				happyNumbers.extend(cache[:-1])
				return True
			elif x in unhappyNumbers:
				unhappyNumbers.extend(cache[:-1])
				return False
			x=digitSquareSum(x)
			if x in cache:
				unhappyNumbers.extend(cache)
				return False
count=0
for i in xrange(10000,2,-1):
	if isHappyNumber(i):
		count+=1
print count
"""