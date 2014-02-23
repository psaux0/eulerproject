#use a set to put the numbers after one number in, and compute the length
#of each set. The larger the length is, the higher position the number is.
f=open("keylog.txt",'r')
b=set()
c=set()
d=dict()
for line in f:
	b.add(line.strip())
for i in ''.join(b):
	c.add(i)
for i in c:
	d[i]=set()
for i in b:
	for j in xrange(len(i)-1):
		for k in i[j+1:]:
			d[i[j]].add(k)
print ''.join(sorted(list(d),key=lambda x: len(d[x]),reverse=True))

#an interesting method
keyFile = open('keylog.txt')

random.seed()

logins = list()

for line in keyFile:
   logins.append(int(line))

# Looks for number in remaining digits of passcode, if not there, inserts a new number at current spot
import random
def passcodeFromList(logins):

   passcode = list();

   for login in logins:

      subIdx = 0

      for char in str(login):
         if char in passcode[subIdx:]:
            subIdx = passcode[subIdx:].index(char) + subIdx + 1
         else:
            passcode.insert(subIdx,char)
            subIdx = subIdx + 1

   return passcode

# Randomly permute the list. Print out the shortest code that was generated
def anneal(loginList, starts, iters):

   best = passcodeFromList(loginList)

   lCopy = loginList[:]

   for x in range(0,starts):
      random.shuffle(lCopy)

      trialBest = passcodeFromList(lCopy)

      for y in range(0,iters):
         temp = lCopy.pop(random.randrange(len(lCopy)))
         lCopy.insert(random.randrange(len(lCopy)),temp)

         temp2 = passcodeFromList(lCopy)
         if len(temp2) < len(trialBest):
            trialBest = temp2

      if len(trialBest) < len(best):
         best = trialBest

   return best

print(anneal(logins, 100, 100))