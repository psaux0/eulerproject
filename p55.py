def isNotLychrel(n):
	t=str(n)
	r=''.join(reversed(t))
	k=0
	while True:
		b=int(t)+int(r)
		if str(b) == ''.join(reversed(str(b))):
			return True
		t=str(b)
		r=''.join(reversed(t))
		k+=1
		if k>50:
			return False

count=0
for i in xrange(1,10001):
	if isNotLychrel(i):
		count+=1
print 10000-count

#a better solution using "for-loop" instead of "while-loop"
def Lycheck(n):
    for i in range(0,50):
        n = n+int(str(n)[::-1])
        if str(n)==str(n)[::-1]: return False
    return True
print len([n for n in range(10000) if Lycheck(n)])