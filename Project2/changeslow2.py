#!/usr/bin/env python

def changeslow_rec(amount, coins, coinsUsed):
	num_coins = 0
	coinCount = len(coins)
	for i in reversed(coins):
		coinCount-=1
		if amount == i:
			coinsUsed[coinCount]+=1
			num_coins = sum(coinsUsed)
			return num_coins, coinsUsed
	for i in reversed(coins):
		coinCount-=1
		if i < amount: #coin value is less than amount
			coinsUsed[coinCount]+=1
			amount = amount-i
			changeslow_rec(amount, coins, coinsUsed)
			num_coins = sum(coinsUsed)
			return num_coins, coinsUsed
	return num_coins, coinsUsed			

def changeslow(array, value):
    coins = [0 for x in range(len(array))]
    print(changeslow_rec(value, array, coins))

a = [1, 5, 10, 25, 50]

changeslow(a, 100)
