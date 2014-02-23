cache={1:[3,2]}
def sqrtTwo(n):
	if n in cache:
		return cache[n]
	else:
		x=[sum(sqrtTwo(n-1))+sqrtTwo(n-1)[1],sum(sqrtTwo(n-1))]
		cache[n]=x
		return x

def numMoreThanDenum(arr):
	return len(str(arr[0]))>len(str(arr[1]))

count=0
for i in xrange(1,1001):
	if numMoreThanDenum(sqrtTwo(i)):
		count+=1

print count