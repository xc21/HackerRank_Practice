# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 22:21:08 2017

@author: Xun Cao
"""

from math import sqrt

N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]

mu = sum(arr)/float(N)

diff_sq = [(i-mu)**2 for i in arr]

stdev = sqrt(sum(diff_sq)/float(N))

print('{0:.1f}'.format(stdev))