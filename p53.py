from time import time
t1=time()
def C(n,r):
	w,t=1,1
	for i in xrange(r):
		w*=n-i
		t*=(i+1)
	return w/t

def overOneMillion(x):
	y=0
	for i in xrange(4,x/2+1):
		if C(x,i)>1000000:
			y=i
			break
	if y==0:
		return 0
	else:
		w=x-y
		return w-y+1

k=0
for i in xrange(1,101):
	k+=overOneMillion(i)

t2=time()
print k,t2-t1
