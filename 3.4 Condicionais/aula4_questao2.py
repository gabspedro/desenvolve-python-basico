print("Qual sua Nota para o Filme: De Volta Para o Futuro")
nota = int(input())

if nota == 0:
    print("Você considera o filme Muito Ruim!")
elif nota == 1:
    print("Você considera o filme Ruim!")
elif nota == 2:
    print("Você considera o filme Regular!")
elif nota == 3:
    print("Você considera o filme Bom!")
elif nota == 4:
    print("Você considera o filme Bom Muito!")
elif nota == 5:
    print("Você considera o filme Excelente!")
else:
    print("Você colocou uma nota invalida.")