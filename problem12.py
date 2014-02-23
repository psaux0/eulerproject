#calculate how many divisible numbers are there of a number
def dNumber(num):
	dNum=0
	for i in xrange(1,int(num**0.5)+1):
		if num/i*i==num:
			dNum+=1
	return dNum*2

p=0

while True:
	numSum=sum(range(p))
	if dNumber(numSum) >= 500:
		print numSum
		break
	p+=1

