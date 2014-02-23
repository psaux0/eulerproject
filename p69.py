def primes(n):
	p=[1]*(n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if p[i/2]:
			p[i*i/2::i]=[0]*((n-i*i-1)/(2*i)+1)
	return [2]+[2*i+1 for i in xrange(1,n/2) if p[i]]

p=primes(10000)

xxx=1
for i in p:
	xxx*=i
	if xxx>1000000:
		print xxx/i
		break

#a number "n" which equals to the product of all prime numbers less than this number will not be prime with all the numbers(expect prime ones),because it
#contains all the possible factors that these numbers might have. For this reason, n/phi(n) is the smallest

