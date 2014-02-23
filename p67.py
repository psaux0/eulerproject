s=[]
with open("triangle.txt","r") as triangle:
	for line in triangle:
		s.append(line.split())

for i in s:
	for j in xrange(len(i)):
		if i[j].startswith('0'):
			i[j]=int(i[j][1:])
		else:
			i[j]=int(i[j])

def merge(sOne,sTwo):
	for i in xrange(len(sOne)):
		if sTwo[i]>=sTwo[i+1]:
			sOne[i]+=sTwo[i]
		else:
			sOne[i]+=sTwo[i+1]

#start merging
for i in xrange(len(s),1,-1):
	merge(s[i-2],s[i-1])
	s.pop()

print s