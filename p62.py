cache=dict()
number=dict()
for i in xrange(100,10000):
	w=i*i*i
	t=list(str(w))
	t.sort()
	k=''.join(t)
	if k in cache:
		cache[k]+=1
		number[k].append(i)
	else:
		cache[k]=1
		number[k]=[i]
	if cache[k]==5:
		print w,number[k][0]**3
		break

#a piece of 16-line python code, took 68ms to run.
#I realized that testing whether a number is perfect cube or not is not a good idea.
#I just compute the cube of numbers from 100 to 10000 and check whether they have same digits by sorting them and comparing the lists made of these numbers in python. I recorded the times that same digits occur in a dictionary and the keys of this dictionary are the strings made from cubes.


#quote: sort it first!