nivel = input("Qual o seu tipo de assinatura? ").lower().strip()
faturamento = float(input("Qual o seu faturamento anual? "))
valor = 0
if nivel == "basic":
    valor = faturamento * 1.3
elif nivel == "silver":
    valor = faturamento * 1.2
elif nivel == "gold":
    valor = faturamento * 1.1
elif nivel == "platinum":
    valor = faturamento * 1.05
else:
    input("Nome inválido! Opções: basic, silver, gold, platinum.")
print(f"Valor do faturamento: {valor:.2f}")

