from collections import Counter
from urllib2 import urlopen
 
file_url = 'http://projecteuler.net/project/poker.txt'
hands = (line.split() for line in urlopen(file_url))
 
values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]
 
def hand_rank(hand):
	score = zip(*sorted(((v, values[k]) for
		k,v in Counter(x[0] for x in hand).items()), reverse=True))
	score[0] = ranks.index(score[0])
	if len(set(card[1] for card in hand)) == 1: score[0] = 5 #flush
	if score[1] in straights: score[0] = 8 if score[0] == 5 else 4 #str./str. flush
	return score
 
print "Answer to PE54 =", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)

#The first tuple would consist between 2 and 5 elements representing the frequency of card values sorted in descending order. The second tuple would consist of the same number of elements as the first but describe the value sorted and weighted by frequency in descending order.