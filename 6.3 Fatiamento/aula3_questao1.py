n = int(input())
lista = []

while n != 0 or len(lista) < 4:
    n = int(input())
    lista.append(n)

print(f"A Lista Original: {lista}")
print(lista[:3:1]) # Os três primeiros números
print(lista[-2::]) # Os dois últimos números
print(lista[::-1]) # O inverso da lista
print(lista[::2]) # Os números pares da lista
print(lista[1::2]) # Os números ímpares da lista