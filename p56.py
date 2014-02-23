w=set()
for a in xrange(1,100):
	for b in xrange(1,100):
		w.add(a**b)

def digitSum(n):
	return sum([int(x) for x in str(n)])


ans=0

for i in w:
	tmp=digitSum(i)
	if tmp>ans:
		ans=tmp
print ans
