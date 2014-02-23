def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]

primeList=[x for x in primes(1000000) if x>100000]

#filt out all the numbers which don't have three or more same numbers
#if a number only has one or two same numbers, there couldn't be 8 values in a family, at most 7(by testing whether it can divide 3)
def three(n):
	x=str(n)
	for i in x:
		if x.count(i)>2:
			return True
	return False

goodNumbers=filter(three,primeList)

#replace the common digits of all numbers so that we can check the rest digits are same by sorting them
def cool(n):
	x=str(n)
	k=0
	for i in x:
		if x.count(i)>2:
			k=i
			return x.replace(k,'-')
	return x


betterNumbers=map(cool,goodNumbers)
betterNumbers.sort()
bestNumbers=list()

#after sorting, we call these strings "keys", if one key occurs more than 6 times, we record it.(since there might be some numbers that have four same digits, and these digits are all replaced by '-')
for i in set(betterNumbers):
	if betterNumbers.count(i)>=6:
		bestNumbers.append(i)

#compare if a number and a key are the same at positions which are not '-'
def compare(a,b):
	for i in xrange(len(b)):
		if b[i] == '-' or a[i]==b[i]:
			continue
		else:
			return False
	return True

#test a number whether positions that are '-' in a key are the same digit in this number
def anotherCompare(a,b):
	for i in xrange(len(b)):
		if b[i]=='-':
			if a[i]!=a[b.index('-')]:
				return False
	return True

#main loop
for j in bestNumbers:
	total=0
	for i in goodNumbers:
		if compare(str(i),j) and anotherCompare(str(i),j):
			print i
			total+=1
	print "key:%s,total:%s" %(j,total)
	print "\n"