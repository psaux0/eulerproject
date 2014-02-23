from time import time
t1=time()

def fac(n):
	j=1
	for i in xrange(1,n+1):
		j*=i
	return j

allfact={0:1}
for i in xrange(1,10):
	allfact[i]=fac(i)

l=list()

def facSum(n):
	k=0
	for i in str(n):
		k+=allfact[int(i)]
	return k

for i in xrange(7*fac(9)):
	if i == facSum(i):
		l.append(i)
t2=time()
print sum(l),t2-t1