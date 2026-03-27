print("Bem-vindo(a) à loja FIAP Wear!")
compra = float(input("O valor total da sua compra é de: R$"))
cupom = input("Digite o cupom de desconto: ")
desconto = compra * 0.90
if cupom.upper() == "NIVER10":
    print(f"O desconto é válido. Sua compra ficou no valor de R${desconto:.2f}")
else:
    print(f"O compra ficou no valor de R${compra:.2f}")

