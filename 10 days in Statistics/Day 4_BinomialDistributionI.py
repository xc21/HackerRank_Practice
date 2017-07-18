# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:29:17 2017

@author: caoxun
"""

from math import factorial
def Binomial(i, n, p):
    c = factorial(n)/(factorial(i)*factorial(n-i))
    return c*(p**i)*((1-p)**(n-i))
p = 1.09/(1.09+1)
p_gte3 = Binomial(3,6,p)+Binomial(4,6,p)+Binomial(5,6,p)+Binomial(6,6,p)
print('{0:.3f}'.format(p_gte3))