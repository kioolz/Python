# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:45:50 2019

@author: Caio
"""
#Primeiro defina as variáveis 
print ("Insira a massa da substância")
Massa = float(input())
print ("Insira a quantidade de mols da substância")
Mol = float(input())
print ("Insira o volume da substância")
Volume = float(input())



#Depois, defina a operação que deseja realizar
# Começa a operação que calcula a Massa Molecular da substância e retorna o valor na tela

def MassaMolecular(Massa,Mol):
    MassaMolecular=Massa/Mol
    return("Esta é a massa molecular", MassaMolecular)
MassaMolecular(Massa,Mol)

def Densidade(Massa,Volume):
    
    Densidade=Massa/Volume
    return ("Esta é a densidade", Densidade)


def VolumeEspecifico(Massa,Volume):
    VolumeEspecifico=Volume/Massa
    return("Este é o volume específico", VolumeEspecifico)
    
    
#Código da mistura homogênea    
    
Massaparcial=float
Massatotal=float
Volumeparcial=float
Volumetotal=float
Volume=float
m=float
v=float
DensidadedaSoluçao=float
v = []
m = []
    
def SoluçãoHomog ():
    
    Massaparcial = float(input("Digite as massas [0 para terminar]"))
    Massatotal = 0
    
    while Massaparcial!=0:
        Massatotal = Massaparcial + Massatotal
        Massaparcial = float(input(("Digite o valor da proxima massa ou aperte 0 para terminar")))
        m.append(Massaparcial)
    Volumeparcial = float(input("Digite os volumes [0 para terminar]"))
    Volumetotal = 0
    while Volumeparcial !=0:
        Volumetotal = Volumeparcial + Volumetotal
        Volumeparcial = float(input("Digite o volume parcial da próxima substancia ou aperte 0 para terminar"))
        v.append(Volumeparcial)
    
    if len(m) == len(v):
        DensidadedaSoluçao=Massatotal/Volumetotal
        print ("A massa total é ", Massatotal)
        print ("O volume total é", Volumetotal) 
        print ("A densidade da solução é ", DensidadedaSoluçao)
    else:
        print("Você não inseriu a mesma quantidade de massas e volumes, erro")
    
    
    
   
   
   
#------------------
SoluçãoHomog()



#Existe a possibilidade da massa ser pedida segundo os padrões internacionais
# em gramas ou em libras
# Então é necessário criar 2 classes para as unidades de peso.


# E a partir desta tabela, classificar os átomos segundo suas propriedades
Propriedades = ["Elemento", "Número de Átomos", "Peso Atômico", "Massa(g)"]











    
