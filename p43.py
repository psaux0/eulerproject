def perm(arr, pos = 0):
    if pos == len(arr):
        yield arr
    for i in range(pos, len(arr)):
        arr[pos], arr[i] = arr[i], arr[pos]
        for _ in perm(arr, pos + 1): yield _
        arr[pos], arr[i] = arr[i], arr[pos]

def gotYa(arr):
	k1=int(''.join(arr[1:4]))
	k2=int(''.join(arr[2:5]))
	k3=int(''.join(arr[3:6]))
	k4=int(''.join(arr[4:7]))
	k5=int(''.join(arr[5:8]))
	k6=int(''.join(arr[6:9]))
	k7=int(''.join(arr[7:]))
	return (not k1%2) and (not k2%3) and (not k3%5) and (not k4%7) and (not k5%11) and (not k6%13) and (not k7%17)

num=['0','1','2','3','4','5','6','7','8','9']
total=0
for i in perm(num):
	if i[0]=='0':
		continue
	if gotYa(i):
		x=int(''.join(i))
		total+=x

print total

#one-line use python built-in itertools
print(sum([int(i) for i in list(map(''.join, itertools.permutations('0123456789',10)))if (int(i[1:4]) % 2 == 0) and (int(i[2:5]) % 3 == 0) and (int(i[3:6]) % 5 == 0) and (int(i[4:7]) % 7 == 0) and (int(i[5:8]) % 11 == 0) and (int(i[6:9]) % 13 == 0) and (int(i[7:10]) % 17 == 0)]))
	

#a more pretty version
import sys
from itertools import permutations

DIVISORS = ((1,2), (2,3), (3,5), (4,7), (5,11), (6,13), (7,17))

def is_divisible(n):
    for d, p in DIVISORS:
        if int(n[d:d+3]) % p != 0:
            return False
    return True

def main():
    print sum([ int(''.join(p)) for p in permutations('0123456789') if p[0] != '0' and is_divisible(''.join(p)) ])
        
if __name__ == '__main__':
    sys.exit(main())