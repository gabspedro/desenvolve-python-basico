ano = int(input("Digite o Ano: "))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("É um Ano Bissexto")
else:
    print("Não é um Ano Bissexto")