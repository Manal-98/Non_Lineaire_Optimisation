# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:55:42 2022

@author: manal
"""

def x(n,s,x0):
    if n>0:
        return x0+(n-1)*s
    else:
        return x0+(n+1)*s


def f(n,s,x0):
    return x(n,s,x0)**5-5*x(n,s,x0)**3-20*x(n,s,x0)+5

def p_acc():
    x0=0.0
    s=0.05
    n=1
    if f(2,s,x0)<f(1,s,x0) :
        while f(n+1,s,x0)<f(n,s,x0): 
            n+=1
            s=2*s
        a=x(n-1,s,x0)
        b=x(n,s,x0)
    if f(2,s,x0)>f(1,s,x0):
        while f(n+1,s,x0)>f(n,s,x0):
            n-=1
            s=2*s
        a=x(n-1,s,x0)
        b=x(n,s,x0)
    elif f(2,s,x0)==f(3,s,x0):
        a=x(1,s,x0)
        b=x(2,s,x0)
    elif f(2,s,x0)>f(1,s,x0) and f(2,s,x0)>f(1,s,x0):
        a=x(-2,s,x0)
        b=x(2,s,x0)
    return n,a,b,s

resultat=p_acc()
n=resultat[0]
a=resultat[1]
b=resultat[2]   
s=resultat[3]
print("Le point de minimum x* est compris entre ",a," et ",b)
