form={
	0:"",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen"
}
largeForm={
	2:"twenty",
	3:"thirty",
	4:"forty",
	5:"fifty",
	6:"sixty",
	7:"seventy",
	8:"eighty",
	9:"ninety"
}
def trans(n):
	if n<20:
		return form[n]
	elif n>=20 and n<100:
		q=n/10
		p=n-q*10
		return largeForm[q]+form[p]
	elif n>=100:
		h=n/100
		j=n-h*100
		return form[h]+"hundredand"+trans(j)

print trans(99)

def getTheResult(n):
	x=1
	while x<=n:
		yield len(trans(x))
		x=x+1

print sum(getTheResult(999))+len("onethousand")-9*3
