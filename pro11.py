import time
time1=time.time()
def matrixMax(m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]):
	k=1
	base=list()	
	for i in m:
		k=1
		for j in i:
			k*=j
		base.append(k)

	for i in xrange(4):
		k=1
		for j in xrange(4):
			k*=m[j][i]
		base.append(k)

	k=1	
	for i in xrange(4):
		k*=m[i][i]
	base.append(k)

	k=1
	for i in xrange(4):
		k*=m[3-i][i]
	base.append(k)

	return max(base)

def buildMatrix(matrix,m,n):
	matri=list()
	for i in xrange(m,m+4):
		matri.append([matrix[i][n],matrix[i][n+1],matrix[i][n+2],matrix[i][n+3]])
	return matri


calGrid=list()
with open("../11.txt","rw") as grid:
	for line in grid:
		if line.endswith("\n"):
			line=line[:len(line)-1]
		calGrid.append(line)

for i in xrange(len(calGrid)):
	calGrid[i]=calGrid[i].split()

for hor in xrange(len(calGrid)):
	for ver in xrange(len(calGrid[hor])):
		if calGrid[hor][ver].startswith('0'):
			calGrid[hor][ver]=(calGrid[hor][ver])[1:]
		calGrid[hor][ver]=int(calGrid[hor][ver])

largest=list()
for _i in xrange(17):
	for _j in xrange(17):
		largest.append(matrixMax(buildMatrix(calGrid,_i,_j)))
print max(largest)
time2=time.time()
print time2-time1