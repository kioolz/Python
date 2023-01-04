# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:37:26 2019

@author: Caio
"""


#---------------------------------------------------------------------------------------------

#Exemplo de função de segundo grau com os parâmetros definidos ---
# Próximo passo é colocar um botão para o usuário definir cada parâmetro da variável
# Colocar um comando que printe o gráfico da função de segundo grau.

from math import sqrt

a=-1 ; b=88550000; c=-1;

y1=(-b+sqrt(b*b-4*a*c))/(2*a)
y2=(-b-sqrt(b*b-4*a*c))/(2*a)

y1a=2*c/(-b-sqrt(b*b-4*a*c))
y2a=2*c/(-b+sqrt(b*b-4*a*c))
print('Raiz 1 =', y1, 'Raiz 1 alternativa=' , y1a)
print('Raiz 2 =', y2, 'Raiz 2 alternativa=' , y2a)


#--------------------------------------------------------------------------------------#