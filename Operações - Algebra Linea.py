# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:39:00 2019

@author: Caio
"""


#Script usado para treinar Algebra Linear 

# A Algebra Linear é o ramo da matemática que lida com espaços vetoriais


# Definindo a Adição entre as componentes  
def vector_add(v,w):
    "Soma dos elementos correspondentes"
    return[v_i + w_i for v_i, w_i in zip(v,w)]
    
    
# Definindo a Subtração entre dois vetores
def vector_sub(v,w):
    "Subtrai os elementos correspondentes"
    return [v_i - w_i for v_i, w_i in zip(v,w)]


# Definindo Um novo vetor com a soma dos vetores 
    def vector_sum(vectors):
        "Soma todos os elementos correspondentes"
        result = vectors[0]
        for vector in vectors[1:]:
            result = vector_add(result,vector)
        return result
    
    
# Definindo a multiplicação por um escalar 
        def scalar_multiply(c, v):
            return [ c* v_i for v_i in v]
        
        
        
        


