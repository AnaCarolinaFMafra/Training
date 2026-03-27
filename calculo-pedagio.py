print("CALCULADORA DE PEDÁGIO")
km = float(input("Informe a distância que será percorrida: "))
if km <= 100:
    pedagio = 10
    print(f"O valor do pedágio será de R${pedagio:.2f} reais.")
elif 100 < km < 200:
    pedagio = 20
    print(f"O valor do pedágio será de R${pedagio:.2f} reais.")
else:
    pedagio = 30
    print(f"O valor do pedágio será de R${pedagio:.2f} reais.")