def fullperm(arr,pos=0):
	if pos == len(arr):
		yield arr
	for i in xrange(pos,len(arr)):
		arr[pos],arr[i] = arr[i],arr[pos]
		for _ in fullperm(arr,pos+1): yield _
		arr[pos],arr[i] = arr[i],arr[pos]

def isPandigital(arr):
	a1,b1,c1 = int(''.join(arr[0:2])),int(''.join(arr[2:5])),int(''.join(arr[5:9]))
	a2,b2,c2 = int(''.join(arr[0])),int(''.join(arr[1:5])),int(''.join(arr[5:9]))
	if a1*b1 == c1:
		return c1
	elif a2*b2 == c2:
		return c2
	else:
		return False

a=['3','9','1','8','6','7','2','5','4']

w=set()

for i in fullperm(a):
	if isPandigital(i):
		w.add(isPandigital(i))

print sum(w)


#python has a permutation tool
from itertools import permutations
import time

start=time.clock()
result=0
baseR = []
basem = [
    a * 100 + b * 10 + c
    for a, b, c in permutations(range(1, 9), 3)
]
basen = [
    a * 10 + b
    for a, b in permutations(range(1, 9), 2)
]


basem.extend([i for i in range(1234, 1987) if str(i).find('0')==-1 and len(str(i))==len(set(str(i)))])
basen.extend([i for i in range(1, 10)])

zippedlst = [
    (x,  y) for x in basem for y in basen
    if not set(str(x)) & set(str(y))
]
for (x, y) in zippedlst:
    pkg=str(x)+str(y)+str(x*y)
    if (len(pkg)==len(set(pkg))) and not set(pkg).intersection('0') and len(pkg)==9:
        if ( baseR.count(x*y)==0):
            baseR.append(x*y)
            result=result+(x*y)

sf=str(time.clock()-start)
print(sf)
print(result)

#another way to solute, brute
products = set()
for a in xrange(2000):
        for b in xrange(a, 2000):
                numStr = str(a) + str(b) + str(a*b)
                length = len(numStr)
                if length < 9:
                        continue
                if length > 9:
                        break
                if sorted(numStr) == ['1','2','3','4','5','6','7','8','9']:
                        products.add(a*b)
print sum(products)