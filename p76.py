w=[1]+[0]*100
print w
for i in xrange(1,100):
	for j in xrange(i,101):
		w[j]+=w[j-i]
print w[len(w)-1]