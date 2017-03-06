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

        print (dist(tspArray[1][1], tspArray[2][1]))

        splt = importFile.split('.')
        outFile = ".tour"
        outFile = importFile+outFile
                        
        #open output file for writing
        if(path.isfile(outFile)):
            os.remove(outFile)
                                
        NewFile = open(outFile, 'w')


        NewFile.close()

args = len(sys.argv)
if args <= 1 or args > 2:
    print("Usage: tsp.py <inputfile>")
else:
    main(str(sys.argv[1]))
