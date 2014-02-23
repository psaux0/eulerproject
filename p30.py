def d(n):
	p=[int(i) for i in str(n)]
	s=0
	for x in p:
		s+=x**5
	return s==n

j=list()
#if sum(digit**5)>the number, the number has to be smaller than 333333
#like 599999's digit sum<5*10**5+5*5<599999  499999's sum< 4**5+5*10**5>499999
for i in xrange(100,500000):
	if d(i):
		j.append(i)
print sum(j)