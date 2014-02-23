from itertools import permutations
octagonal=[i*(3*i-2) for i in xrange(0,100) if i*(3*i-2)>1000 and i*(3*i-2)<10000]

def isHeptagonal(n):
	tmp=(40*n+9)**0.5
	return tmp==int(tmp) and tmp%10==7

def isHexagonal(n):
	tmp=(8*n+1)**0.5
	return tmp==int(tmp) and tmp%4==3

def isPentagonal(n):
	tmp=(24*n+1)**0.5
	return tmp==int(tmp) and tmp%6==5

def isSquare(n):
	tmp=n**0.5
	return tmp==int(tmp)

def isTriangle(n):
	tmp=(8*n+1)**0.5
	return tmp==int(tmp) and tmp%2==1

def isOctagonal(n):
	tmp=(3*n+1)**0.5
	return tmp==int(tmp) and tmp%3==2


funcTable={'4':isHeptagonal,'3':isHexagonal,'2':isPentagonal,'1':isSquare,'5':isTriangle,'6':isOctagonal}

def matchNext(arr,n):
	nextArr=list()
	cache=set()
	for i in arr:
		if int(str(i)[2:])<10:
			continue
		cache.add(int(str(i)[2:]))
	for j in cache:
		for k in xrange(j*100,j*100+101):
			if funcTable[n](k):
				nextArr.append(k)
	return nextArr

for i in permutations('12345'):
	arr=octagonal
	for j in i:
		arr=matchNext(arr,j)
	step=list(i)
	x=arr
	if not x:
		continue
	w=matchNext(arr,'6')
	#if w:
		#print w
	for n in step:
		w=matchNext(w,n)
	if len(set(w) & set(x))==1:
		final=matchNext(w,'6')
		if final:
			print final,step

uu=[1281]
s=uu[0]
for x in '32514':
	uu=matchNext(uu,x)
	s+=uu[0]
print s

#a better idea by using position caculation
formulae=[
  lambda n: n*(n+1)//2,
  lambda n: n*n,
  lambda n: n*(3*n-1)//2,
  lambda n: n*(2*n-1),
  lambda n: n*(5*n-3)//2,
  lambda n: n*(3*n-2)
]

numbers=[(f(n)//100,f(n)%100,1<<i) for i,f in enumerate(formulae) for n in range(15,150) if 1000<=f(n)<=9999]
  
def dfs(a,b,head,sig):
  if sig==0b111111:
    if b==head:
      return 100*a+b
    else: return False
  for (a2,b2,sig2) in numbers:
    if b!=a2 or sig==sig|sig2: continue
    res=dfs(a2,b2,head,sig|sig2)
    if res:
      return 100*a+b+res
  return False
  
for a,b,sig in numbers:
  res=dfs(a,b,a,sig)
  if res:
    print(res)
    break

#recursive
f=lambda m,n:n*((m-2)*n+4-m)//2

fourdigits=lambda l:[x for x in l if 1000<=x<10000]

ls=[fourdigits([f(i,n)for n in range(150)])for i in (3,4,5,6,7,8)]
s8=ls.pop()

relie=lambda x,y:x%100==y//100

def extend(lz,ll):
    if ll==[] and len(lz)==6 and relie(lz[-1],lz[0]):yield lz    
    for l in ll:
        for z in l:
            if relie(lz[-1],z):
                ll2=ll[:];ll2.remove(l)
                for x in extend(lz+[z],ll2):yield x
for x in s8:
    for l in extend([x],ls):print(l,sum(l))