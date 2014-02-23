#initiate matrix
matrix=list()
with open("matrix.txt","r") as f:
	for line in f:
		matrix.append(line.strip().split(','))

for i in matrix:
	for j in xrange(len(i)):
		i[j]=int(i[j])

#make it into a diamond
diamondMatrix=list()
for i in xrange(len(matrix)):
	tmp=list()
	for j in xrange(i+1):
		tmp.append(matrix[i-j][j])
	diamondMatrix.append(tmp)

for i in xrange(len(matrix),2*len(matrix)-1):
	tmp=list()
	for j in xrange(i+1-len(matrix),len(matrix)):
		tmp.append(matrix[i-j][j])
	diamondMatrix.append(tmp)

def mergeI(arrOne,arrTwo):
	arrOne[0]+=arrTwo[0]
	arrOne[len(arrOne)-1]+=arrTwo[len(arrTwo)-1]
	for i in xrange(1,len(arrOne)-1):
		if arrTwo[i-1]<=arrTwo[i]:
			arrOne[i]+=arrTwo[i-1]
		else:
			arrOne[i]+=arrTwo[i]

def mergeII(arrOne,arrTwo):
	for i in xrange(len(arrOne)):
		if arrTwo[i+1]<=arrTwo[i]:
			arrOne[i]+=arrTwo[i+1]
		else:
			arrOne[i]+=arrTwo[i]

for i in xrange(157,78,-1):
	mergeI(diamondMatrix[i],diamondMatrix[i+1])
	diamondMatrix.pop()
for i in xrange(78,-1,-1):
	mergeII(diamondMatrix[i],diamondMatrix[i+1])
	diamondMatrix.pop()

print diamondMatrix

#dynamic programming

matrix = [map(int, (lines.split(','))) for lines in open('files/81.dat', 'r')]

for row in xrange(len(matrix)):
        for col in xrange(len(matrix[0])):
                if row == 0 and col == 0:
                        continue
                elif row == 0:
                        matrix[row][col] += matrix[row][col-1]
                elif col == 0:
                        matrix[row][col] += matrix[row-1][col]
                else:
                        matrix[row][col] += min(matrix[row-1][col], matrix[row][col-1])
print matrix[-1][-1]