#!/usr/bin/env python3

from TrackLib import *
from sys import argv, exit
import csv

script, first, second = 'traks.csv',0,2

if len(argv)==2:
    if argv[1]=="--help" or argv[1]=="-h":
        print("Enter the name of the path to the .css file and the route numbers in it for comparison, the numbers should start with 1 and go in order.")
        exit(0)

if len(argv)==4:
    script= argv[1]
    first = int(argv[2])-1
    second= int(argv[3])-1
elif len(argv)!=1:
    print("Input number track to comparations")
    exit(0)

tracks=[]
with open(script) as File:
    r = csv.reader(File, delimiter=';', quotechar=';',
                        quoting=csv.QUOTE_MINIMAL)
    reader = list(r)
    for i in range(1, int(reader[len(reader)-1][0])+1):
        l=[Dot(float(reader[j][2]),float(reader[j][3])) for j in range(1, len(reader)) if int(reader[j][0]) == i]
        tracks.append(l)
print(Matches_All(tracks[first], tracks[second]))
