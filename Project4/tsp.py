#!/usr/bin/env python

from os import path
import time
import os
import sys
import math

#function returns the rounded distace between two points.
def dist(pI, pII):
    out = math.sqrt((pI[0] - pII[0])**2 + (pI[1] - pII[1])**2)
    return int(round(out))

def inDist(pI, pII):
    return dist(pI[1], pII[1])


def tspHeuristic(pointsArray):
    travelDist = 0
    start = pointsArray[0]
    visitPath = pointsArray
    path = [start]
    visitPath.remove(start)
    while visitPath:
        next = min(visitPath, key=lambda x: inDist(path[-1], x))
        travelDist += inDist(path[-1], next)
        path.append(next)
        visitPath.remove(next)
    return path, travelDist


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
        tpsH, distance = tspHeuristic(tspArray)
        print(time.time()-start)
        
        
        splt = importFile.split('.')
        outFile = ".tour"
        outFile = importFile+outFile
                        
        #open output file for writing
        if(path.isfile(outFile)):
            os.remove(outFile)
                                
        NewFile = open(outFile, 'w')
        NewFile.write("%d\n" % distance)
        for x in range(len(tpsH)):
            NewFile.write("%s\n" % tpsH[x][0])

        NewFile.close()

args = len(sys.argv)
if args <= 1 or args > 2:
    print("Usage: tsp.py <inputfile>")
else:
    main(str(sys.argv[1]))
