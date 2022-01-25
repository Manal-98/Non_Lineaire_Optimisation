# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:55:40 2022

@author: manal
"""

def x(n):
    if n>0:
        return x0+(n-1)*pas
    else:
        return x0+(n+1)*pas


def f(n):
    return x(n)**5-5*x(n)**3-20*x(n)+5

def pas_fixe():
    n=1
    if f(2)<f(1) :
        while f(n+1)<f(n): 
            n+=1
        y=x(n-1)
        z=x(n)
    elif f(2)>f(1):
        while f(n+1)>f(n):
            n-=1
        y=x(n-1)
        z=x(n)
    elif f(2)==f(3):
        y=x(1)
        z=x(2)
    elif f(2)>f(1) and f(2)>f(1):
        y=x(-2)
        z=x(2)
    return n,y,z


pas=float(input("Veuillez entrer le pas :"))
x0=float(input("Veuillez entrer la valeur initiale :"))

r=pas_fixe()
n=r[0]
y=r[1]
z=r[2]   
print("X* est compris entre ",y," et ",z," avec f(x*)=",f(n))
                 
             

    