# Entrada

nota1 = float(input("Insira a Nota da Primeira Prova: "))
nota2 = float(input("Insira a Nota da Segunda Prova: "))
nota3 = float(input("Insira a Nota da Segunda Prova: "))
media = (nota1 + nota2 + nota3)/3
print("\n")

# Processamento

while media >= 60:

# Saída

    print("Aprovado!")
    print("Fim!")
    break
else:
    while media >= 40 and media < 60:
    
    # Saída

        print("Recuperação!")
        print("Fim!")
        break
    else:

    # Saída

        print("Reprovado!")
        print("Fim!")