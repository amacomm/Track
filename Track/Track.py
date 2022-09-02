from TrackLib import *
import csv


tracks=[]
with open('traks.csv') as File:
    r = csv.reader(File, delimiter=';', quotechar=';',
                        quoting=csv.QUOTE_MINIMAL)
    reader = list(r)
    for i in range(1, int(reader[len(reader)-1][0])+1):
        l=[Dot(float(reader[j][2]),float(reader[j][3])) for j in range(1, len(reader)) if int(reader[j][0]) == i]
        tracks.append(l)
print(Matches_All(tracks[0], tracks[2]))
