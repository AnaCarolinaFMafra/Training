# Ler a quantia
quantia = int(input("Digite o valor em: R$"))
# Calcular a quantia de cédulas de 100
ced100 = quantia // 100
# Atualizar a quantia
quantia = quantia % 100
# Calcular a quantia de cédulas de 50
ced50 = quantia // 50
# Atualizar a quantia
quantia = quantia % 50
# Calcular a quantia de cédulas de 20
ced20 = quantia // 20
# Atualizar a quantia
quantia = quantia % 20
# Calcular a quantia de cédulas de 10
ced10 = quantia // 10
# Atualizar a quantia
quantia = quantia % 10

print(f"A quantidade de cédulas de 100 foi de {ced100}, de 50 foi de {ced50}, de 20 foi de {ced20} e de 10 foi de {ced10}")