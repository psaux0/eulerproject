k=list()
with open("../yiwan.txt","r") as yiwan:
	for line in yiwan:
		if line.endswith("\n"):
			line=line[:len(line)-1]
		k.append(line)
for i in xrange(len(k)):
	k[i]=int(k[i])
print str(sum(k))[:10]
