import time
t1=time.time()

#a great algorithm making full perm of an array
def perm(arr, pos = 0):
    if pos == len(arr):
        yield arr
    for i in range(pos, len(arr)):
        arr[pos], arr[i] = arr[i], arr[pos]
        for _ in perm(arr, pos + 1): yield _
        arr[pos], arr[i] = arr[i], arr[pos]
 
def isPrime(n):
	if not n%2:
		return False
	for i in xrange(3,int(n**0.5)+1,2):
		if not n%i:
			return False
	return True

io=list()
for i in (7,4):
	y=range(1,i)
	for j in perm(y):
		t=[i]
		t.extend(j)
		n=int(''.join([str(k) for k in t]))
		if isPrime(n):
			l=io.append(n)

t2=time.time()
print max(io),t2-t1