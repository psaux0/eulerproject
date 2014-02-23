count=0
for i in xrange(1,10):
	j=1
	while len(str(i**j))>=j:
		if len(str(i**j))==j:
			count+=1
		j+=1

print count

