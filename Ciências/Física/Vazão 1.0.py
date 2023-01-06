# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:47:47 2019

@author: Caio
"""


class Vazão():
    
    def VazãoVolumetrica():
        
        T=float(input()) #Tempo que levou para que o fluido fosse transportado
        print(T)
        V=float(input()) #Volume transportado por unidade de tempo
        print(V)
        
        F=V/T # A vazão que transporta um certo volume ao longo de um certo tempo
        
                  
        return print(F)

Vazão.VazãoVolumetrica()

    
    
    
    