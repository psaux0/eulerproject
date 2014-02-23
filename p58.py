totalPrimes=0
totalDig=1
k=3

def isPrime(x):
	if not x%2:
		return False
	for i in xrange(3,int(x**0.5)+1,2):
		if not x%i:
			return False
	return True

while True:
	l=k*k-(k-1)
	m=k*k-2*(k-1)
	n=k*k-3*(k-1)
	if isPrime(l):
		totalPrimes+=1
	if isPrime(m):
		totalPrimes+=1
	if isPrime(n):
		totalPrimes+=1
	totalDig+=4
	if totalPrimes*1.0/totalDig<=0.10:
		break
	k+=2

print k

#do not use list if you wanna have a high speed
#find the recursive relations
#use variables to store variables instead of put them all in a list or an array