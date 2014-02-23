import time
time1=time.time()
def distinctPrimes(n):
	f=2
	while f*f<=n:
		while not n%f:
			yield f
			n//=f
		f+=1
	if n>1:
		yield n

def four(x):
	return len(set(i for i in distinctPrimes(x)))==4

j=210
while True:
	if four(j) and four(j+1) and four(j+2) and four(j+3):
		print j
		break
	j+=1

time2=time.time()
print time2-time1