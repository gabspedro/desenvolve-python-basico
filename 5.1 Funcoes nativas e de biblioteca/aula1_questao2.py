import random
import math

soma = 0
valor = 0
cont = 0

n = int(input("Digite Quantas Repetições Você Deseja: "))

for raiz in range(n):
    valor = random.randint(1, 100)
    print(valor)
    
    soma += valor
    cont += 1

print(f"O Resultado da Raiz Quadrada é: {math.sqrt(soma) / cont}")
