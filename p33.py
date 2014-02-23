from time import time
t1=time()
#compare two fractions
def fractions(a,b):
	return a[0]*b[1]==a[1]*b[0]

def simplify(a):
	q=[0,0]
	tmpN=set([x for x in str(a[0])])
	tmpD=set([x for x in str(a[1])])
	w=tmpD & tmpN
	if w and w!=set('0'):
		m=list(w)[0]
		k=list(str(a[0]))
		l=list(str(a[1]))
		k.remove(m)
		l.remove(m)
		q[0]=int(k[0])
		q[1]=int(l[0])
		return q
	else:
		return False	

de=list()
no=list()
for j in xrange(10,100):
	for i in xrange(10,j):
		f=[i,j]
		s=simplify(f)
		if s and fractions(f,s):
			no.append(f[0])
			de.append(f[1])

def gcd(a,b):
	r=a%b
	if r:
		return gcd(b,r)
	else:
		return b

def multi(s):
	return reduce(lambda x,y:x*y,s)

pDe=multi(de)
pNo=multi(no)

g=gcd(pNo,pDe)
ans=pDe/g
t2=time()
print ans,t2-t1