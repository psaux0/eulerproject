def coin(LIMIT):
	p=[1]+[0]*LIMIT
	for i in xrange(1,LIMIT):
		for j in xrange(i,LIMIT+1):
			p[j]+=p[j-i]
	p[-1]+=1
	return p

for i in coin(10001):
	if not i%1000000:
		print i