# Neste problema sua tarefa será ler vários números 
# e em seguida dizer quantas vezes cada número aparece na entrada de dados,
# ou seja, deve-se escrever cada um dos valores distintos que aparecem na entrada por ordem crescente de valor.
# A entrada contém apenas 1 caso de teste. A primeira linha de entrada contém um único
# inteiro N, que indica a quantidade de valores que serão lidos para X (1 ≤ X ≤ 2000) logo
# em seguida. Com certeza cada número não aparecerá mais do que 20 vezes na entrada de
# dados.
# Saída
# Imprima a saída de acordo com o exemplo fornecido abaixo, indicando quantas vezes
# cada um deles aparece na entrada por ordem crescente de valor.
import random
from random import randint

# define a função fun(x):

#Essa é uma função que cria uma lista e preenche ela com valores de 1 a 2000, todos valores inteiros.
def aleatorio(n):
    #Criei uma lista vazia
    X = [] #Lista = []
           #dicionario = {}
    for i in range(n): #range = intervalo
        X.append(randint(1,2000)) 
    return X
y = aleatorio(random.randrange(1,2000))
# s = aleatorio("string")
z = sorted(y)
print("Esta não é a lista ordenada em ordem crescente", y)
print("Esta é a lista ordenada em ordem crescente", z)
cont = 0
def repeticao():
    for i in range(len(y)):
        for j in range(len(y)):
            if y[i] == z[j]:
                cont = cont+1
    return cont

print(repeticao())


    


        











