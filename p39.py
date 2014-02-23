def calC(a,b):
	c=(a*a+b*b)**0.5
	if c == int(c):
		return c
	else :
		return False

p=120

def triNumbers(p):
	count=0
	for m in xrange(int(p/4),int(p/2)):
		for n in xrange(m):
			if not calC(m,n):
				continue
			elif calC(m,n)+m+n==p:
				count+=1
			else:
				pass
	return count

MAX=0
NUM=0

for p in xrange(100,1000):
	tmp=triNumbers(p)
	if tmp>MAX:
		MAX=tmp
		NUM=p

print NUM,MAX

#a better solution generating pythagorean triples
def problem39():
    ret = 0
    maximum = 0
    for p in range(4,1001,2):
        sol = 0
        for a in range(1,p//3):
            if(p*(p-2*a) % (2*(p-a)) == 0): sol += 1
        if sol>maximum:
            maximum = sol
            ret = p
    return ret

#a even better solution using euclid's formula

import time

def gcd(a,b):
   while b != 0: 
      t = b
      b ,a = a%b, t
   return a

t0=time.clock()	
m,p_dict,k = 2,{},True	

while k:
   n=1
   while n < m:
      if (m-n)%2 ==0 : 
         n+=1
         continue
      elif gcd(m,n)!=1:
         n+=1
         continue
      abc=[]		
      abc.append(m**2 - n**2);abc.append(2*m*n);abc.append(m**2 + n**2)
      k ,p = 1,0
      p = k*(abc[0]+abc[1]+abc[2])
      if p>1000: 
         k=False
         break
      while 1:
         p = k*(abc[0]+abc[1]+abc[2])
         if p>1000:break
         elif not p_dict.has_key(p): p_dict[p] = 1
         else: p_dict[p] += 1
         k+=1
      n+=1	
   else: m+=1	
for i in p_dict:
   if p_dict[i]==max(p_dict.values()):
      print "Ans: ",i,"\nDur: ",time.clock()-t0
      break