from time import time
t1=time()
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def nameScore(s):
	nS=0
	for i in s:
		nS+=alp.index(i)+1
	return nS

f=open("names.txt","r")
output=0

j=f.readline().split(',')
j.sort()

for i in xrange(len(j)):
	k=j[i].strip('"')
	output+=(nameScore(k)*(i+1))

t2=time()
print output, t2-t1

