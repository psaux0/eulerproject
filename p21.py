from time import time
time1=time()
#brute way to get all factors by using generator
def factors(n):
	k=1
	while k<n:
		if not n%k:
			yield k
		k+=1

x=list()
for i in xrange(10000):
	f=sum(factors(i))
	if i == sum(factors(f)) and f!=i:
		x.append(i)
s=sum(x)
time2=time()
print s, time2-time1, x



#a better solution
#the best solution is to store the number of factors of small numbers in a list,and then 
# when calculate large numbers' factors, we can use the list to look for it and save time
tStart = time()

def d(number):
    
    divisors = []
    square_root = sqrt(number)
    
    for i in range(1, int(square_root)):
        if number % i == 0:
            divisors.append(i)
    
    for i in divisors[1:len(divisors)]:
        divisors.append(number / i)
        
    if square_root % 1 == 0:
        divisors.append(int(square_root))
        
    return sum(divisors)

amicable_numbers = [i for i in xrange(2, 10000 + 1) if \
                    d(d(i)) == i and d(i) != i]
                    

print sum(amicable_numbers)
print "Run Time = " + str(time() - tStart) 