# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:36:28 2017

@author: Xun Cao
"""

#weighted average
N = int(input().strip())

x_arr = [int(i) for i in input().strip().split(' ')]
w_arr = [int(i) for i in input().strip().split(' ')]

run_sum = 0

for i in range(N):
    run_sum += x_arr[i]*w_arr[i]
    
print('{0:.1f}'.format(run_sum/sum(w_arr)))
