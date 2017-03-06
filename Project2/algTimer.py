#!/usr/bin/env python

from sys import maxint
from os import path
import numpy as np
import time

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
    return changeslow_rec(value, array, coins)


def changedp(array, value):
    coinCount = len(array)-1
    coins = [0 for x in range(coinCount+1)]
    coinUsed = [0 for x in range(value+1)]
    minCoin = [0 for x in range(value+1)]
    for x in range(value+1):
        coinCount = x
        newCoin = 1
        for j in [c for c in array if c <= x]:
            if minCoin[x-j] + 1 < coinCount:
                coinCount = minCoin[x-j]+1
                newCoin = j
            minCoin[x] = coinCount
            coinUsed[x] = newCoin
    return minCoin[value], coins

def changegreedy(array, value):
    sum = value
    coinCount = len(array)-1
    num_Coins = 0
    coins = [0 for x in range(coinCount+1)]
    while coinCount >= 0:
        while sum >= array[coinCount]:
            sum -= array[coinCount]
            coins[coinCount]+=1
            num_Coins+=1
        coinCount-=1
    return num_Coins, coins


outFile = "Time_Results.txt"


#open output file for writing
NewFile = open(outFile, 'w')

A=[]

#A is array of values to make change from.  modify below to change range( <start value>, <end value>, <increment>)
A.extend(range(1,1001,1000))

# V is change array
V = []
V.extend(range(1,247,5))
print(V)
         


NewFile.write("changeslow:\n")
for i in range(len(A)):
    start = time.time()
    m, coins = changeslow(V, A[i])
    tTime = time.time() - start
    NewFile.write("%d\t%f\t%d\n" % (A[i], tTime, m))


NewFile.write('\n')
NewFile.write("changegreedy:\n")
for i in range(len(A)):
    start = time.time()
    m, coins = changegreedy(V, A[i])
    tTime = time.time() - start
    NewFile.write("%d\t%f\t%d\n" % (A[i], tTime, m))

NewFile.write('\n')
NewFile.write("changedp:\n")
for i in range(len(A)):
    start = time.time()
    m, coins = changedp(V, A[i])
    tTime = time.time() - start
    NewFile.write("%d\t%f\t%d\n" % (A[i], tTime, m))


NewFile.close()

