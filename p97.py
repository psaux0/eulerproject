def digitsMulti(a,b):
	c=a*b
	if c>10**10:
		c=c%(10**10)
	return c

def digitPow(a,x):
	j=1
	for i in xrange(x):
		j=digitsMulti(j,a)
	return j

m=digitPow(2,7830457)
n=digitsMulti(m,28433)

print n+1