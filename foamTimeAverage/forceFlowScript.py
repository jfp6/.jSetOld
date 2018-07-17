#!/usr/bin/env python

import csv

files = ['flow0m.txt','flow1m.txt','flow2m.txt','flow3m.txt']
for fi in files:
    with open(fi,'rb') as csvfile: 
        lines = csv.reader(csvfile,delimiter='=')
        summ = 0 
        count = 0
        for i,line in enumerate(lines):
            if i>0:
                linem = line[-1].split('(')
                linemm = linem[1].split(' ')
                summ += float(linemm[0])
                count += 1
        print(fi,summ/count,summ/count*15850)

files = ['jet0m.txt','jet1m.txt','jet2m.txt','jet3m.txt']
for fi in files:
    with open(fi,'rb') as csvfile: 
        lines = csv.reader(csvfile,delimiter='=')
        summ = 0 
        count = 0
        for i,line in enumerate(lines):
            if i>0:
                summ += float(line[-1])
                count += 1
        print(fi,summ/count,summ/count/4.448)




