def C(k,x=2):
	m,n=1,1
	for i in xrange(x):
		m*=k-i
		n*=i+1
	return m/n

a=10**12+1
b=10**12

def hugeNumber(n):
	i=1
	while i<=n:
		yield i
		i+=1

for i in hugeNumber(10**12):
	c=b+i
	d=c-1
	w=c*d/2
	if w==int(w**0.5)*(int(w**0.5)+1):
		print c
		break
