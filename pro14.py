import time
time1=time.time()
#even or odd
"""
def isEven(n):
	return n/2*2==n

def trans(n):
	if isEven(n):
		n=n/2
	else:
		n=3*n+1
	return n

def keepTrans(n):
	count=0
	while not n==1:
		n=trans(n)
		count=count+1
	return count

k=1
l=0
for i in xrange(1000000-1,500000,-2):
	j=keepTrans(i)
	if j>k:
		k=j
		l=i
print l
time2=time.time()
print time2-time1
"""

"""
  A better solution use recursive and the most important part is use global table to store the numbers which have been calculated
"""
table={1:1}
def col(n):
	x=0
	if n in table:
		return table[n]
	elif n%2:
		x=1+col(3*n+1)
	else:
		x=1+col(n/2)
	table[n]=x
	return x

large=0
num=0
for i in xrange(1,1000000):
	j=col(i)
	if j>large:
		large=j
		num=i

print num
print time.time()-time1