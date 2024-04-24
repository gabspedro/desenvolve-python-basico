# Entrada de Dados

valor = int(input("Digite o Valor: "))

# Processamento dos Dados

##### Centenas

nota_de_100 = int(valor // 100) # 576 // 100 = 5.76 -> 5
valor = valor % 100             # 576 - 5*100 = 76

##### Dezenas

nota_de_50 = int(valor // 50) # 76 // 50 = 1.sla -> 1
valor = valor % 50            # 76 - 1*50 = 26
nota_de_20 = int(valor // 20) # 26 // 20 = 2.3 -> 2
valor = valor % 20            # 6
nota_de_10 = int(valor // 10) # 6 // 10 = 0
valor = valor % 10            # 6

##### Unidades

nota_de_5 = int(valor // 5) # 6 // 5 = 1.sla -> 1
valor = valor % 5           # 6 - 1*5
nota_de_2 = int(valor // 2) # 1 // 21 = 0
valor = valor % 20          # 1
nota_de_1 = int(valor // 1) # 1 // 1 = 1 -> 1
valor = valor % 1           # 1 - 1 = 

# Saída dos Dados

print(f"Notas de 100: {nota_de_100}")
print(f"Notas de 50: {nota_de_50}")
print(f"Notas de 20: {nota_de_20}")
print(f"Notas de 10: {nota_de_10}")
print(f"Notas de 5: {nota_de_5}")
print(f"Notas de 2: {nota_de_2}")
print(f"Notas de 1: {nota_de_1}")