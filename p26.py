import time
t1=time.time()

def gc(d):
	x=9
	z=x
	k=1
	while z%d:
		z=z*10+x
		k+=1
	return k

w=0
out=0
for i in xrange(1,1000):
	if i%2 and i%5:
		tmp=gc(i)
		if tmp>w:
			w=tmp
			out=i
t2=time.time()

#another solution which is much easier to understand
def cyc(n):
    rem = []
    r = 0
    i = 1
    while(i % n not in rem):
        r = i % n
        if r == 0: return 0
        rem.append(r)
        i *= 10
    rem = rem[rem.index(i % n):] #the first one that has same reminder with i%n
    return len(rem) #the length of rem stands for number of repeating digits while numbers in rem stand for nothing(the reminders, if once it's the same as before, a circular begins. if reminder=0,it is finite)
    
cyclist = [cyc(x) for x in range(1,1000)]
t3=time.time()
print cyclist.index(max(cyclist))+1,out,t2-t1,t3-t2

