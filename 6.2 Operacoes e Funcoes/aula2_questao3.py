import random

lista1 = [random.randint(0, 50) for a in range(random.randint(1, 20))]
lista2 = [random.randint(0, 50) for a in range(len(lista1))]

inters = []
for elemento in lista1:
    if elemento in lista2:
        inters.append(elemento)


print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print("\n")
print(f"Intersecção Ordenada: {sorted(inters)}")
print("\n")

for n in inters:
    print(f"{n}: Lista 1 = {lista1.count(n)} | Lista 2 = {lista2.count(n)}")