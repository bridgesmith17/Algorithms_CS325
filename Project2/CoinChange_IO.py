#!/usr/bin/env python

from os import path
import time
import os
import sys



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
    coinLoc = value
    while coinLoc > 0:
        coinVal = coinUsed[coinLoc]
        for x in range(len(array)):
            if (array[x] == coinVal):
                coins[x]+=1
        coinLoc -= coinVal
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


def main (importFile):
    #open test problem file and import into testArray
    if (path.isfile(importFile)):
        testFile = open(importFile, 'r')
        testArray = []
        for line in testFile:
            newLine = line.rstrip('\n')
            newLine = newLine.rstrip('\r')
            newLine = newLine.split()
            x = len(newLine)
            i = 0
            while i < x:
                newLine[i] = int(newLine[i])
                i+=1
            testArray.append(newLine)
        
        testFile.close()
        
        
        #create output file name by using input file name + change.txt
        splt = importFile.split('.')
        outFile = "change.txt"
        outFile = splt[0]+outFile
        
        #open output file for writing
        if(path.isfile(outFile)):
            os.remove(outFile)
        
        NewFile = open(outFile, 'w')
        
        
        #loop through testArray Writing data into output file
        NewFile.write("Algorithm slowchange:\n")
        i=0
        #change slow loop
        while i < len(testArray):
            for x in range(len(testArray[i])):
                NewFile.write("%d " % testArray[i][x])
            NewFile.write('\n')
            value = testArray[i+1]
            m, coins = changeslow(testArray[i],value[0])
            for x in range(len(coins)):
                NewFile.write("%d " % coins[x])
            NewFile.write('\n')
            NewFile.write("%d" % m)
            NewFile.write('\n')
            i+=2
        NewFile.write('\n')
        NewFile.write('\n')
        NewFile.write("Algorithm changedp:\n")
        i=0
        #changedp loop
        while i < len(testArray):
            for x in range(len(testArray[i])):
                NewFile.write("%d " % testArray[i][x])
            value = testArray[i+1]
            NewFile.write('\n')
            m, coins = changedp(testArray[i],value[0])
            for x in range(len(coins)):
                NewFile.write("%d " % coins[x])
            NewFile.write('\n')
            NewFile.write("%d" % m)
            NewFile.write('\n')
            i+=2
        NewFile.write('\n')
        NewFile.write('\n')
        NewFile.write("Algorithm changegreedy:\n")
        i=0
        #changegreedy loop
        while i < len(testArray):
            for x in range(len(testArray[i])):
                NewFile.write("%d " % testArray[i][x])
            value = testArray[i+1]
            NewFile.write('\n')
            m, coins = changegreedy(testArray[i],value[0])
            for x in range(len(coins)):
                NewFile.write("%d " % coins[x])
            NewFile.write('\n')
            NewFile.write("%d" % m)
            NewFile.write('\n')
            i+=2
        NewFile.write('\n')
        NewFile.write('\n')
        
        NewFile.close()




args = len(sys.argv)
if args <= 1 or args > 2:
    print("Usage: CoinChange_IO.py <inputfile>")
else:
    main(str(sys.argv[1]))
