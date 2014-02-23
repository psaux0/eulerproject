from itertools import cycle
f=open("cipher1.txt","r")
k=[int(i) for i in f.readline().split(',')]
keyOne=[k[i] for i in xrange(len(k)) if not i%3]
keyTwo=[k[i] for i in xrange(len(k)) if i%3==1]
keyThree=[k[i] for i in xrange(len(k)) if i%3==2]

alphabet='abcdefghijklmnopqrstuvwxyz'

def cipherKey(num):
	key=''
	smallest=500
	for i in alphabet:
		cipherNumber=0
		rr=ord(i)
		for j in num:
			m=rr^j
			if (m<ord("A") or m>ord("z")) and m!=ord(' '):
				cipherNumber+=1
		if cipherNumber<smallest:
			smallest=cipherNumber
			key=i
	return key

key=''.join((cipherKey(keyOne),cipherKey(keyTwo),cipherKey(keyThree)))

print key

n=0
s=list()
asiisum=0
for item in cycle(key):
	asiisum+=ord(item)^k[n]
	s.append(chr(ord(item)^k[n]))
	n+=1
	if n>len(k)-1:
		break
print ''.join(s)
print asiisum

"""
First, I tried to use all letters to decrypt keyOne,keyTwo,keyThree, and I always get one letter, whose results contain the least [^A-Za-z ] letters, much less than others, and I know this is the answer. So I got my code.
"""

