# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:23:50 2017

@author: Martin
"""

a = 4
b = 4
while b>0:
    while a>0:
        print ('*', end='')
        a = a-1
    print (end='\n')
    b = b-1
    a = b
print (end='\n')

a = 4
b = 4
c = 1
d = 1
x = 5
while x>0:
    while a>0:
        print (' ', end='')
        a = a-1
    while c>0:
        print ('*', end='')
        c = c-1
    print (end='\n')
    b = b-1
    a = b
    d = d+2
    c = d
    x = x-1
print (end='\n')

a = 1
b = 1
c = 1
while a>0:
    c = a
    while c>0:
        print ('*', end='')
        c = c-1
    a = a+b
    if (a>3):
        b = -1
    print (end='\n')
print (end='\n')