# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:13:30 2017

@author: Xun Cao
"""

#median, mean, mode challenge

from statistics import mean,median,mode

N = int(input().strip())

## MEAN
# convert the input (string) to list 
arr = [int(i) for i in input().strip().split(' ')]
#use the array.sort to arrange all i in ascending order 
arr.sort()

#sum over the array and divide by the given number
print('{0:.1f}'.format(sum(arr)/N))

## MEDIAN
#for even number
if N % 2 == 1:
    print('{0:.1f}'.format(arr[int((N-1)/2)]))
else:
    #for odd number
    print('{0:.1f}'.format(0.5*(arr[int(N/2)-1]+arr[int(N/2)])))

## MODE    
counts=[]
for i in arr:
    counts.append(arr.count(i))
if max(counts) > 1:
    #.index
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))
