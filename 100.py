from time import time
time1=time()
x=list()
with open("../1000.txt","r") as txt:
    for line in txt:
        if line.endswith("\n"):
            line=line[:len(line)-2]
            x.append(line)
        x.append(line)
y=''.join(x)
fin=list(y)
larger=0
for an in xrange(996):
    phi=int(fin[an])*int(fin[an+1])*int(fin[an+2])*int(fin[an+3])*int(fin[an+4])
    if phi > larger:
        larger=phi
print larger

time2=time()
print time2-time1
