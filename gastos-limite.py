print("CONTROLADOR DE DESPESAS")
limite_despesas = 3000
despesas = float(input("Digite o valor total das suas despesas: "))
if despesas > limite_despesas:
    print("Você excedeu o limite de gastos mensais.")
else:
    print("Você conseguiu economizar!")