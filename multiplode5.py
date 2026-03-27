# Ler um número dado pelo usuário
# Calcular o próximo múltiplo de 5
# Exibir o próximo múltiplo de 5

numero_usuario = int(input("Digite um número inteiro qualquer: "))
proximo_mult_5 = numero_usuario // 5 * 5 + 5
print(f"O próximo múltiplo de 5 seguinte ao número dado pelo usuário é: {proximo_mult_5}")
