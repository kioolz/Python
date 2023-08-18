# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:40:35 2019

@author: Caio
"""

from numpy.lib.scimath import sqrt

def raizQuadrada():
    a = float(input("Insira o valor da constante A"))
    b = float(input("Insira o valor da constante B"))
    c = float(input("Insira o valor d"))

a = 1  
b = 2
c = 100 

# Coeficientes polinômiais



r1 = (-b+sqrt(b**2-4*a*c))/(2*a)
r2 = (-b-sqrt(b**2-4*a*c))/(2*a)

print(r1)
print(r2)