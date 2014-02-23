def lversion(n):
	return sorted([x for x in str(n)])

def samedigits(x):
	return lversion(2*x)==lversion(3*x)==lversion(4*x)==lversion(5*x)==lversion(6*x)

x=100

while not samedigits(x):
	x=x+1

print x
