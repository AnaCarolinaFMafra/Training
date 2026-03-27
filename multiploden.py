# Ler um número dado pelo usuário
# Calcular o próximo múltiplo de um número sugerido pelo usuário
# Exibir o próximo múltiplo do número sugerido

numero_usuario = int(input("Digite um número inteiro qualquer: "))
numero_multiplo = int(input("Digite outro número inteiro: "))
multi = numero_usuario // numero_multiplo * numero_multiplo + numero_multiplo
print(f"O próximo múltiplo de {numero_multiplo} seguinte ao número dado pelo usuário é: {multi}")