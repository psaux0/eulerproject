def isPentagon(n):
	w=(24*n+1)**0.5
	if w == int(w) and w%6==5:
		return True
	else:
		return False

def P(n):
	return n*(3*n-1)/2

def f(x):
	w=x
	while True:
		for i in xrange(w-1,0,-1):
			if isPentagon(P(w)-P(i)) and isPentagon(P(w)+P(i)):
				return P(w)-P(i)
		w=w+1

print f(10)