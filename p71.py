from fractions import gcd
n=1000000/7
de=n*7
nu=n*3
while gcd(nu,de)!=1:
	nu-=1
print nu