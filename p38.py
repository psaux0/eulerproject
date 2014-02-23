import time
t1=time.time()
for i in xrange(9200,9500):
	k=i*2
	c=str(i)+str(k)
	if len(c) == len(set(c)):
		print c
t2=time.time()
print t2-t1