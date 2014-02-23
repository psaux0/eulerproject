from time import time
t1=time()
def fac(n):
	p=1
	for i in xrange(1,n+1):
		p*=i
	return p

l=[0,1,2,3,4,5,6,7,8,9]

s=1000000
k=list()



while s>0:
	j=fac(len(l)-1)
	d=s/j
	if s<=j*d:
		print s,l
		break
	k.append(l[d])
	l.remove(l[d])
	s=s-d*j

t2=time()
print k, t2-t1


"""
Python. It can be refined to be perfect(but I am too tired now) 
four outputs, the last one is time,the last list stands 
for the number in order,the second list stands for a list 
not in order. What I need to do is to combine the last 
list with the 4th(the first number) smallest number made 
by digits from second list which is 460 
( first 046, second 064, third 406, forth 460), 
here's the result then 4 [0, 4, 6] [2, 7, 8, 3, 9, 1, 5] 
time:7.79628753662e-05~0.00008s
"""