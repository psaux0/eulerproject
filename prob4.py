def isPalin(num):
	x=list(str(num))
	x.reverse()
	return num==int("".join(x))

for i in xrange(1000,99,-1):
	for j in xrange(1000,99,-1):
		if isPalin(i*j):
			print i*j
			break
#something wrong here