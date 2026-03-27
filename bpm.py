idade = float(input("Informe a idade (em anos, ex: 0.5 para 6 meses): "))
frequencia = int(input("Informe a frequência cardíaca (BPM): "))

if 0 <= idade <= 0.08:  # 0 a 28 dias
    min_f, max_f = 100, 205

elif 0.08 < idade <= 1:  # 28 dias a 1 ano
    min_f, max_f = 100, 180

elif 1 < idade <= 3:
    min_f, max_f = 98, 140

elif 3 < idade <= 5:
    min_f, max_f = 80, 120

elif 5 < idade <= 12:
    min_f, max_f = 75, 118

elif idade >= 13:
    min_f, max_f = 60, 100

else:
    print("Idade inválida.")
    exit()
if min_f <= frequencia <= max_f:
    print("DENTRO DA FAIXA ADEQUADA.")
elif frequencia < min_f:
    print("ABAIXO DA FAIXA ADEQUADA.")
else:
    print("ACIMA DA FAIXA ADEQUADA.")
