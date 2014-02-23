from time import time

time1=time()
s="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#text filter
s=s.split("\n")
for i in range(len(s)):
	s[i]=s[i].split()
for i in s:
	for j in range(len(i)):
		if i[j].startswith("0"):
			i[j]=i[j][1:]
		i[j]=int(i[j])

#merge function
def merge(sOne,sTwo):
	for i in xrange(len(sOne)):
		if sTwo[i]>=sTwo[i+1]:
			sOne[i]+=sTwo[i]
		else:
			sOne[i]+=sTwo[i+1]

#start merging
for i in xrange(len(s),1,-1):
	merge(s[i-2],s[i-1])
	s.pop()

time2=time()
print s,time2-time1

# Merge the second last row with the final one, since every 
# node in the second last row only has one choice. After merging, 
# they become one row. just do it again and again