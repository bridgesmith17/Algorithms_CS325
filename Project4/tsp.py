#!/usr/bin/env python

from os import path
import time
import os
import sys
import math
import random
import copy

#function returns the rounded distace between two points.
def dist(pI, pII):
    out = math.sqrt((pI[0] - pII[0])**2 + (pI[1] - pII[1])**2)
    return int(round(out))

#helper function to pass coordinates inside array to dist function
def inDist(pI, pII):
    return dist(pI[1], pII[1])

#greedy path, uses list in order given to find the next closest location and add to path
#based on :https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm
def tspNN(pointsArray, start):
    travelDist = 0
    start = pointsArray[start]
    visitPath = pointsArray
    path = [start]
    visitPath.remove(start)
    while visitPath:
        next = min(visitPath, key=lambda x: inDist(path[-1], x))
        travelDist += inDist(path[-1], next)
        path.append(next)
        visitPath.remove(next)
    #add in final distance from last to first location
    travelDist += inDist(path[0], path[-1])
    return path, travelDist

#getDist loops though ordered array of tsp path to calcualted the total distance traveled
def getDist(pointsArray):
    i = 1
    travelDist = 0
    while i <= len(pointsArray)-1:
        travelDist += inDist(pointsArray[i-1], pointsArray[i])
        i+=1
    travelDist += inDist(pointsArray[0], pointsArray[-1])
    return travelDist

#two opt pulls checks and compares two the distance of two points and swaps if necessary to get the shortest path
#based on: https://en.wikipedia.org/wiki/2-opt, https://github.com/ntrifunovic/TSP/blob/master/tsp.py
def two_opt(pointsArray):
    for i in range(len(pointsArray) - 1):
        for j in range(i + 2, len(pointsArray) - 1):
            if (inDist(pointsArray[i], pointsArray[i+1]) + inDist(pointsArray[j], pointsArray[j+1]) > inDist(pointsArray[i], pointsArray[j]) + inDist(pointsArray[i+1], pointsArray[j+1])):
                pointsArray[i+1:j+1] = reversed(pointsArray[i+1:j+1])
    dist = getDist(pointsArray)
    return pointsArray, dist

#three opt similar to 2-opt checks three distances at a time to find the shortest path
#based on: https://en.wikipedia.org/wiki/3-opt, https://github.com/ntrifunovic/TSP/blob/master/tsp.py
def three_opt(pointsArray):
    for i in range(len(pointsArray) - 1):
        for j in range(i + 2, len(pointsArray) - 1):
            for k in range(j + 2, len(pointsArray) - 1):
                way = 0
                current = inDist(pointsArray[i], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[k + 1])
                if current > inDist(pointsArray[i], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[k + 1])
                    way = 1
                if current > inDist(pointsArray[i], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[k + 1])
                    way = 2
                if current > inDist(pointsArray[i], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[k + 1])
                    way = 3
                if current > inDist(pointsArray[i], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[k + 1])
                    way = 4
                if current > inDist(pointsArray[i], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[j + 1]) + inDist(pointsArray[k], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[k + 1])
                    way = 5
                if current > inDist(pointsArray[i], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[k]) + inDist(pointsArray[k], pointsArray[i + 1]) + inDist(pointsArray[j], pointsArray[k + 1])
                    way = 6
                if current > inDist(pointsArray[i], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[k + 1]):
                    current = inDist(pointsArray[i], pointsArray[k]) + inDist(pointsArray[j + 1], pointsArray[j]) + inDist(pointsArray[i + 1], pointsArray[k + 1])
                    way = 7
                if way == 1:
                    pointsArray[j + 1: k + 1] = reversed(pointsArray[j + 1: k + 1])
                elif way == 2:
                    pointsArray[i + 1: j + 1] = reversed(pointsArray[i + 1: j + 1])
                elif way == 3:
                    pointsArray[i + 1: j + 1], pointsArray[j + 1: k + 1] = reversed(pointsArray[i + 1: j + 1]), reversed(pointsArray[j + 1: k + 1])
                elif way == 4:
                    pointsArray = pointsArray[: i + 1] + pointsArray[j + 1: k + 1] + pointsArray[i + 1: j + 1] + pointsArray[k + 1: ]
                elif way == 5:
                    temp = pointsArray[: i + 1] + pointsArray[j + 1: k + 1]
                    temp += reversed(pointsArray[i + 1: j + 1])
                    temp += pointsArray[k + 1: ]
                    pointsArray = temp
                elif way == 6:
                    temp = pointsArray[: i + 1]
                    temp += reversed(pointsArray[j + 1: k + 1])
                    temp += pointsArray[i + 1: j + 1]
                    temp += pointsArray[k + 1: ]
                    pointsArray = temp
                elif way == 7:
                    temp = pointsArray[: i + 1]
                    temp += reversed(pointsArray[j + 1: k + 1])
                    temp += reversed(pointsArray[i + 1: j + 1])
                    temp += pointsArray[k + 1: ]
                    pointsArray = temp
    dist = getDist(pointsArray)
    return pointsArray, dist



#uses tspNN function and adds a random start point to find the best path, varies number of random starts based on size of input to reduce time of operation
def randScale(pointsArray):
    min_dist= 100000000
    n = len(pointsArray)-1
    if n > 10000:
        r = 5
    elif n > 4000:
        r = 10
    elif n > 1000:
        r = 20
    elif n > 50:
        r = 50
    else:
        r = n
    for i in range(r):
        x = random.randint(0,n)
        pointsArray, dist = tspNN(pointsArray, x)
        if (dist < min_dist):
            min_dist = dist
            min_array = copy.copy(pointsArray)
        print (i)
    return pointsArray, min_dist


#main function reads input file with path, inserts into array and passes to tsp function.  It then creats output file of best path found by algorithm
def main (importFile):
    #open test problem file and import
    if (path.isfile(importFile)):
        testFile = open(importFile, 'r')
        tspArray = []
        #import file line into tspArray in form [city, [x, y]]
        for line in testFile:
            newLine = line.rstrip('\n')
            newLine = newLine.rstrip('\r')
            newLine = newLine.split()
            coord = [int(newLine[1]), int(newLine[2])]
            temp = [newLine[0], coord]
            tspArray.append(temp)

        testFile.close()
        
        #time and call tsp function
        start = time.time()
        tspF, distance = randScale(tspArray)
        print(time.time()-start)
        
        splt = importFile.split('.')
        outFile = ".tour"
        outFile = importFile+outFile
                        
        #open output file for writing
        if(path.isfile(outFile)):
            os.remove(outFile)
                                
        NewFile = open(outFile, 'w')
        NewFile.write("%d\n" % distance)
        for x in range(len(tspF)):
            NewFile.write("%s\n" % tspF[x][0])

        NewFile.close()

args = len(sys.argv)
if args <= 1 or args > 2:
    print("Usage: tsp.py <inputfile>")
else:
    main(str(sys.argv[1]))
