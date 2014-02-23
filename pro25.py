import time
time1=time.time()
table={1:1,2:1}
def fab(n):
	if n in table:
		return table[n]
	else:
		x=fab(n-1)+fab(n-2)
		table[n]=x
		return x

k=12
while len(str(fab(k)))<=999:
	k+=1
print k
time2=time.time()
print time2-time1


#a better soluntion 
pair=[1,1]
i=3
while pair[0]+pair[1] < 10**999:
    pair[i%2]+=pair[(i+1)%2]
    i+=1
print i
time3=time.time()
print time3-time2

# When you don't have to care about the other numbers in a squence,
# just let them go