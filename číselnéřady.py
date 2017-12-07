# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:49:57 2017

@author: Martin
"""

import random
# generuje 20 náhodných čísel od 1 do 50 
seznam = [random.randint(1,50) for i in range(20)]
print ('seznam celých kladných čísel')
for x in range (0,20):
    print (seznam[x], end=' ')
print ()
print ()

# generuje 20 náhodných čísel od -50 do 50 
seznam2 = [random.randint(-50,50) for i in range(20)]

print ('seznam celých čísel')
for x in range (0,20):
    print (seznam2[x], end=' ')
print ()
print ()

print ('první příklad')
n = 0
for x in range (0,20):
    if (seznam[x]/2 == int(seznam[x]/2)):
        n = n+1
print ('počet sudých čísel (ze seznamu kladných čísel) je',n)
print ()

print ('druhý příklad (čísla mezi 11 a 19 ze seznamu kladných čísel):')
for x in range (0,20):
    if (seznam[x]>10 and seznam[x]<20):
        print (seznam[x], end=' ')
print ()
print ()

print ('třetí příklad (čísla dělitelná zároveň 3 a 4 z kladných čísel):')
for x in range (0,20):
    if (seznam[x]/12 == int(seznam[x]/12)):
        print (seznam[x], end=' ')
print ()
print ()


print ('čtvrtý příklad')
k = 0
z = 0
for x in range (0,20):
    if (seznam2[x]>0):
        k = k+seznam2[x]
    else:
        z = z+seznam2[x]            
print ('součet kladných čísel',k)
print ('součet záporných čísel',z)
print ()

print ('pátý příklad')
m = 0
for x in range (0,20):
    m = m+(seznam2[x]*seznam2[x])
print ('součet druhých mocnin celých čísel je',m)
print ()

print('šestý příklad')
s = 0
for x in seznam:
    s = s + x
p = s / len(seznam)
print('aritmetický průměr kladných čísel je', p)
