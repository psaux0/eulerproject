from time import time
t1=time()

def triangleSum(n):
	return n*(n+1)/2

def isTriangle(n):
	for i in xrange(int(n**0.5),int((2*n)**0.5)+1):
		if triangleSum(i) == n:
			return True
	return False

#print isTriangle(55),isTriangle(45),isTriangle(29)

ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def nameToNumber(s):
	y=0
	s=s.strip('"')
	for i in list(s):
		y+=ALPHA.index(i)+1
	return y

f=open("words.txt","r")
n=f.readline()
line=n.split(',')

count=0
for i in line:
	k=nameToNumber(i)
	if isTriangle(k):
		count+=1
t2=time()
print count,t2-t1
