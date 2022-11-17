class Conta: # Característica da conta bancária
    def __init__(self, numero, cpf, nomeTitular, saldo): #Parâmetros
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

#botões do caixa eletrônico
def depositar(self, valor):
        self.saldo += valor

def sacar(self, valor):
        self.saldo -= valor

def gerarextrato(self):
    print(f"numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}")


conta1 = Conta(1, 123, "joao", 500)
conta2 = Conta(2, 321, "bola", 1200)



print(conta1.saldo)
print(conta1)

print(type(conta1))

