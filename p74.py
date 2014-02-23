def factorial(x):
	uu=1
	for i in xrange(1,x+1):
		uu*=i
	return uu

facs=dict()
facs[0]=1
for i in xrange(1,10):
	facs[i]=factorial(i)

def facSum(n):
	return sum([facs[int(i)] for i in str(n)])

def step(n):
	tmp=list()
	x=n
	i=0
	tmp.append(x)
	while True:
		x=facSum(x)
		i+=1
		if x in tmp:
			break
		tmp.append(x)
	return len(tmp)

count=0
for i in xrange(1,1000001):
	if step(i)==60:
		count+=1
print count
"""
An alternative idea: store the values that comes out
I Made a array containing 1.000.000 zeroes, put the known values in, and looped through the array. Finaly I counted all elements equal to 60.
"""

"""
My approach was to find combinations of numbers that met the criteria. Due to the commutative property of addition, it doesn't matter what order the numbers appear (except for a 0 at the beginning). So if any combination (note the 0 exception case), has a chain of 60, all permutations will as well. After you figure out what permutations meet the criteria, some math will help you determine the number of combinations that can be generated which can be added to give you the final answer.
"""
import math
import itertools

# since all factorials are 9 or less, just store them.
fact = [1,1,2,6,24,120,720,5040,40320,362880]

def getFactorialChainLength(n, MAX=60):
    seen = []
    chainCount = 1
    testNum = n
    while True:
        if chainCount > MAX:
            break

        result = 0
        for digit in str(testNum):
            result += fact[int(digit)]

        if result in seen:
            break

        chainCount += 1
        seen.append(result)
        testNum = result

    return chainCount


resultMap = {}

for l in xrange(1, 7):
    for p in itertools.combinations_with_replacement("0123456789", l):
        testStr = ''.join(p)

        if (int(testStr) == 0):
            continue

        while testStr[0] == '0':
            testStr = testStr[1:] + '0'

        testKey = int(''.join(sorted(testStr, reverse=True)))
        if testKey in resultMap:
            continue

        testNum = int(testStr)
        chainCount = getFactorialChainLength(testNum)

        resultMap[testKey] = chainCount

sixtyChainCount = 0
for key in resultMap.keys():
    if resultMap[key] == 60:
        combinations = math.factorial(len(str(key)))

        # since  the number 0 has no effect at the beginning, remove
        # all combinations that account for 0; note this may happen
        # multiple times for numbers containing more than one '0'
        for c in str(key):
            if c == '0':
                combinations -= fact[len(str(key)) - 1]

        repeatCount = len(str(key)) - len(set(str(key)))
        if (repeatCount > 0):
            combinations /= (2 * repeatCount)

        sixtyChainCount += combinations

print "Count = %d" % sixtyChainCount