print("CALCULADORA DE NOTAS ENSINO MÉDIO")
nota_1 = float(input("Informe a sua 1ª nota: "))
nota_2 = float(input("Informe a sua 2ª nota: "))
nota_3 = float(input("Informe a sua 3ª nota: "))
media = (nota_1 + nota_2 + nota_3)/3
if media >= 7:
    print("Parabéns! Você está aprovado.")
elif 5 <= media < 7:
    print("Ops! Você está de recuperação.")
else: 
    print("Infelizmente você está reprovado.")