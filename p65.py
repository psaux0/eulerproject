from fractions import gcd

def upSideDown(arr):
	arr.reverse()
	return arr

def fractionSum(a,b):
	de=a[1]*b[1]
	nu=a[1]*b[0]+a[0]*b[1]
	tmp=gcd(de,nu)
	return [nu/tmp,de/tmp]

def getE(n):
	if n==1:
		return [1,1]
	elif n%3==2:
		if 99-n+1<3:
			t1=99-n
		else:
			t1=(99-n+2)//3
		t2=[2*t1,1]
		return upSideDown(fractionSum(t2,getE(n-1)))
	else:
		return upSideDown(fractionSum([1,1],getE(n-1)))

ans=fractionSum([2,1],getE(99))
print sum(int(i) for i in str(ans[0]))