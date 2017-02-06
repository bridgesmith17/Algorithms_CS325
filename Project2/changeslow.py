#!/usr/bin/env python

def changeslow(amount, coins):

#if there is a k cent coin thent that one is the minimum
	coins_size = 0
	num_coins = 0
	for i in coins:
		coins_size = coins_size + 1
		if amount == i:
			num_coins = 1
			print i
			return num_coins
	
	
	print  coins_size
	return num_coins

	for i in coins:
		if amount > i:
			 


print changeslow(26, [1, 5, 10, 25, 50])




#attempt at Divide and Conquer version

def changeslowH(array, value):
    minCoin = value
    for i in range(len(array)):
        if (array[i] == value):
            depth = 0
            return 1
    else:
        for x in [c for c in array if c <= value]:
            coinCount = changeslowH(array, value-x)
            coinCount+=1
            if (coinCount < minCoin):
                minCoin = coinCount

    return minCoin

def changeslow(array, value):
    coins = [0 for x in range(len(array))]
    print(changeslowH(array, value))

