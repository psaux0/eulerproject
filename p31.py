count=0
for i in xrange(3):
	for j in xrange(5):
		for l in xrange(11):
			for m in xrange(21):
				for n in xrange(41):
					for p in xrange(101):
						if i*100+j*50+l*20+m*10+n*5+p*2<=200:
							count+=1

print count

#a much better classical solution
def count_change(money, coins): 
    if money == 0:
        return 1
    elif money < 0 or not coins:
        return 0
    return (count_change(money - coins[0], coins) + 
            count_change(money, coins[1:]))

coins = (1, 2, 5, 10, 20, 50, 100, 200)
count_change(200, coins)

"""
The classic, recursive solution 
(based on the approach of creating a decision tree, 
at every branch of which a coin is chosen or it is not
Such as if you wanna use coin 1, then minus 1 and calculate the whole methods
"""
# other ways
def addcoin(array,n):
    result = [0]*len(array)
    for i in range(len(array)):
        result[i] = array[i]
        for j in range(1,i//n+1):
            result[i] += array[i-j*n]
    return result

array_init = [0]*201
# Array to make the index auf out 1p and 2p coins
for i in range(len(array_init)):
    array_init[i] = i//2 + 1

coins = [5,10,20,50,100,200]

basis = array_init
for i in coins:
    coin_added = addcoin(basis,i)
    basis = coin_added

print(coin_added[200])


#recursive
def coins_sum(coins, target):
    # base case
    if target == 0 or coins[0] == 1:
        global ways
        ways += 1
        return

    for multi in range(target//coins[0],0,-1):
        diff = target - coins[0]*multi
        coins_sum(coins[1:], diff)
    coins_sum(coins[1:], target)

##################################
>>> ways = 0
>>> coins_sum([200, 100, 50, 20, 10, 5, 2, 1], 200)
>>> ways
73682