import random

n = int(input("Quantas Vezes Repetir? "))
lista = [random.randint(-100, 100) for a in range(n)]

print(f"A Lista Ordenada: {sorted(lista)}")
print(f"A Lista Original: {lista}")
print(f"O Maior Valor: {max(lista)}")
print(f"O Menor Valor: {min(lista)}")