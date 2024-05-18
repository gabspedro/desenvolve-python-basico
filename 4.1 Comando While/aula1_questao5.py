n = int(input())

# Variáveis

soma = 0 # Resultado para Soma
cont = 0 # Controle

while cont < n:
    idade = int(input())
    soma += idade # Soma = Soma + Idade

    cont += 1 # Cont = Cont + 1

# Média

print("\n")
print(soma)
print(soma/n)