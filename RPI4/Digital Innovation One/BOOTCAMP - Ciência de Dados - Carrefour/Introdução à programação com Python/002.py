a = int(input('Primeiro bimestre : '))
b = int(input('Segundo semestre: '))
c = int(input('Terceiro semestre: '))
d = int(input('Quarto bimestre: '))
media = (a + b + c + d) / 4
if a < 10 and b < 10 and c < 10 and d < 10:
    print('media: {}'.format(media))
else:
    print('foi informada alguma nota errada')


#Programa que testa se ao menos um número par foi digitado
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')

# #Outra versão do código acima apenas usando o not como negação da afirmação [?]
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')


#Trecho de código para saber se o valor é par ou ímpar
# a = int(input('Digite o valor:'))
# resto = a % 2
# if resto == 0:
#     print('número é par')
# else:
#     print('Número é impar')





# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor:'))
# c = int(input('Terceiro valor: '))

# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))
# print('Final do programa')

# Control + / = Transforma todo código selecionado em comentário

