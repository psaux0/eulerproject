w=1
q=''.join([str(i) for i in xrange(1000000)])	
for i in xrange(7):
	w*=int(q[10**i])

print w
