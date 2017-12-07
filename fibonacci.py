# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:11:14 2017

@author: Martin
"""

n = input('Kolik členů posloupnosti se má tisknout? > ')
n = int(n)
a = 0
b = 1
if n >= 1:
    print (a, end=' ')
if n >= 2:
    print (b, end=' ')

for x in range (2,n):
    c = a+b
    print (c, end=' ')
    a, b  = b, c
print()
