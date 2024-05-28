import random

n = random.randint(1, 10)
resultado = 0

while resultado != n:
    resultado = int(input())

    if resultado == n+1 or resultado == n-1:
        print("Está Próximo")
    elif resultado > n+1 or resultado < n-1:
        print("Muito Longe")
    else:
        print("Correto")
        break
    