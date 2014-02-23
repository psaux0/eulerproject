import time
time1=time.time()
def factor(n):
	f=2
	while f*f<=n:
		while not n%f:
			yield f
			n//=f
		f+=1
	if n>1:
		yield n
print set([x for x in factor(600851475143)])
time2=time.time()
print time2-time1
"""Use a number starting from 2 to divide a large number, the first several ones must be a
prime divider or its multiple number"""