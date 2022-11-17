entrada = float(input("insira o valor do salário"))

if (entrada <= 400.00):
    reajuste = 15/100
    novosal = entrada + (entrada*reajuste)
    print(novosal)
    dif = novosal - entrada
    reajuste = dif/entrada * 100
    print(f"Novo salário:", {novosal:. 2f})
    print(f"Reajuste ganho:", {dif:. 2f})
    print(f"Em percentual:", {reajuste:. 2f},"%")

if (entrada >= 400.01) and (entrada <= 800.00):
    reajuste = 12/100
    novosal = entrada + (entrada*reajuste)
    print(novosal)
    dif = novosal - entrada
    reajuste = dif/entrada * 100
    print(f"Novo salário:", {novosal:. 2f})
    print(f"Reajuste ganho:", {dif:. 2f})
    print(f"Em percentual:", {reajuste:. 2f},"%")

if (entrada >= 800.01) and (entrada <= 1200.00):
    reajuste = 10/100
    novosal = entrada + (entrada*reajuste)
    print(novosal)
    dif = novosal - entrada
    reajuste = dif/entrada * 100
    print(f"Novo salário:", {novosal:. 2f})
    print(f"Reajuste ganho:", {dif:. 2f})
    print(f"Em percentual:", {reajuste:. 2f},"%")

if (entrada >= 1200.01) and (entrada <= 2000.00):
    reajuste = 7/100
    novosal = entrada + (entrada*reajuste)
    print(novosal)
    dif = novosal - entrada
    reajuste = dif/entrada * 100
    print(f"Novo salário:", {novosal:. 2f})
    print(f"Reajuste ganho:", {dif:. 2f})
    print(f"Em percentual:", {reajuste:. 2f},"%")

if (entrada >= 2000.01):
    
    reajuste = 4/100
    novosal = entrada + (entrada*reajuste)
    print(novosal)
    dif = novosal - entrada
    reajuste = dif/entrada * 100
    print(f"Novo salário:", {novosal:. 2f})
    print(f"Reajuste ganho:", {dif:. 2f})
    print(f"Em percentual:", {reajuste:. 2f},"%")
