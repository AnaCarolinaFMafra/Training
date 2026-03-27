# O objetivo é calcular a porcentagem do desconto de um produto!
# Porcentagem não é um operador, mas sim uma expressão, portanto, % não é porcentagem, mas sim resto de.

preço = float(input("Digite o preço do produto: "))
porcentagem = int(input("Digite a porcentagem do desconto: "))
valord = preço - (preço * porcentagem / 100)
print(f"O valor do produto com o desconto será de: {valord:.2f} ")

# Se for acréscimo do valor do produto:

preço = float(input("Digite o preço do produto: "))
porcentagem = int(input("Digite a porcentagem do aumento: "))
valord = preço + (preço * porcentagem / 100)
print(f"O valor do produto com o aumento será de: {valord:.2f} ")
