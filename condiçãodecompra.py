# O usuário irá efetuar uma compra, caso essa compra seja + de 300 reais, ele irá ganhar um desconto de 10%.
# Caso contrário, ele irá pagar o valor total.

valor_compra = float(input("Digite o valor da compra: "))
if valor_compra > 300:
    valor_compra = valor_compra - (valor_compra * 10/100)
    print(f"O valor da compra será de {valor_compra:.2f} reais")
else:
    print("Você não obteve desconto para essa compra.")

# if se a condição for verdadeira
# else se a condição for falsa
# elif senão se (geralmente entre o primeiro if e o else sucessor