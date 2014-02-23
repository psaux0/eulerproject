import time
time1=time.time()

table={1:1}
def fac(n):
	if n in table:
		return table[n]
	else:
		x=n*fac(n-1)
		table[n]=x
		return x


l=list(str(fac(100)))
for i in xrange(len(l)):
	l[i]=int(l[i])

print sum(l)
time2=time.time()
print time2-time1