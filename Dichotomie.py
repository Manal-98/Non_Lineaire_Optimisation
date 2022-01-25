# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:53:28 2022

@author: manal
"""

def fonction(x):
    return x**5 -5*x**3 -20*x +5

def bissec(a,b,epsilon,optimum):
    x0=(a+b)/2
    x1=(a+x0)/2
    x2=(x0+b)/2
    f0 = fonction(x0)
    f1 = fonction(x1)
    f2 = fonction(x2)
    if optimum == 'mini':
        if f2>f0 and f0>f1:
            b=x0
        elif f2<f0 and f0<f1:
            a=x0
        elif f1>f0 and f2>f0:
            a=x1
            b=x2
    elif optimum == 'maxi':
        if f2>f0 and f0>f1:
            a=x0
        elif f2<f0 and f0<f1:
            b=x0
        elif f1>f0 and f2>f0:
            if f1==max(f1,f2):
                b=x1
            else:
                a=x2
    return(a,b)

def biss(a,b,optimum,epsilon):
    while (b-a)>epsilon:
        (a,b)=bissec(a,b,epsilon,optimum)
    print("a={0},b={1},x={2}".format(a,b,(a+b)/2))

biss(0,1,"mini",0.01)