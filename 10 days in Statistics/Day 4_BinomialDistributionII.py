# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:42:33 2017

@author: caoxun
"""
#the binomial function fro previous challenge
from math import factorial
def Binomial(i, n, p):
    c = factorial(n)/(factorial(i)*factorial(n-i))
    return c*(p**i)*((1-p)**(n-i))


p,n = list(map(int, input().split()))
p = p/100

#no more than 2
p_le2 = Binomial(0,10,p)+Binomial(1,10,p)+Binomial(2,10,p)
# at least 2
p_ge2 = 1 - p_le2 + Binomial(2,10,p)
print('{0:.3f}\n{1:.3f}'.format(p_le2, p_ge2))