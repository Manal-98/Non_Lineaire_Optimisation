# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 01:27:06 2022

@author: manal
"""

"""Methode Newton Raphson CAS II"""
# fonction
def f(x):
    return x**3 - 7*x**2 + 8*x - 3 

#dérivé de la fonction
def df(x):
    return 3*x**2 - 14*x + 8
#dérivé seconde de la fonction
def df2(x):
    return 6*x - 14

def xn(i,df,df2,x0):
    if i==1:
        return x0
    else:
        return xn(i-1,df,df2,x0)-(df(xn(i-1,df,df2,x0))/df2(xn(i-1,df,df2,x0)))
    
def NR(x0,eps):
    i=1
    while abs(df(xn(i,df,df2,x0)))>epsilon:
        i+=1
    return xn(i,df,df2,x0)   
  

# l'utilisateur entre ces valeurs
x0 = input('Entrer la valeur initiale: ')
epsilon = input('Erreur approximative: ')

# Converti x0 et e en nombre virgule
x0 = float(x0)
epsilon = float(epsilon)  
# On lance la fonction
print('\nLe résultat de la méthode Newton Raphson est \nx* = ', NR(x0,epsilon))
