sumK=0
for i in xrange(1,1003,2):
	sumK+=i*i

msumk=0
for i in xrange(2,1002,2):
	msumk+=i

print sumK*4-msumk*6-3