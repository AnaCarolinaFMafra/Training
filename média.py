# primeiro passo: ler o primeiro número
# segundo passo: ler o segundo número
# terceiro passo: ler o terceiro número
# quarto passo: calcular a média
# exibir a média

primeironumero = input("Digite o primeiro número: ")
segundonumero = input("Digite o segundo número: ")
terceironumero = input("Digite o terceiro número: ")
media = float(primeironumero + segundonumero + terceironumero) / 3
print(f"O valor da média desses números é: {media:.2f}")