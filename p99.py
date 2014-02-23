import math

#deal with file
b=list()
f=open("base_exp.txt",'r')
k=0
while k<1000:
	b.append(f.readline()[:-1].split(','))
	k+=1
for i in b:
	for j in xrange(len(i)):
		i[j]=int(i[j])

#compare function
def getLn(arr):
	return arr[1]*math.log(arr[0])

m=0
identity=0
for i in b:
	tmp=getLn(i)
	if tmp>m:
		m=tmp
		identity=i
print tmp,b.index(identity),len(b)