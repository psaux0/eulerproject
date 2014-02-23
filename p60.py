def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return (2,)+tuple([2*i+1 for i in xrange(1,n/2) if p[i]])

p=primes(10**6)
bigP=[i for i in p if i>1000]
smallP=[i for i in p if i>1000 and i<10000]
c=dict()
for i in p:
	c[i]=True

def cutX(n):
	a=str(n)[:3]
	b=str(n)[3:]
	if b.startswith('0'):
		return False
	k=int(''.join([a,b]))
	j=int(''.join([b,a]))
	if c.get(k,False) and c.get(j,False) and c.get(int(a),False) and c.get(int(b),False):
		return True,a
	else:
		return False
nnd=dict()
for i in bigP:
	if cutX(i):
		w=str(i)[3:]
		if nnd.setdefault(w,None):
			nnd[w].append(str(i)[:3])
		else:
			nnd[w]=[str(i)[:3]]
bb=list()
for i in nnd:
	for j in nnd:
		x=set(nnd[i]) & set(nnd[j])
		if len(x)>2:
			bb.append((i,j,x))

w=sorted(bb,key=lambda x:int(x[0])+int(x[1])+sum([int(i) for i in x[2]]))
print w[0]