# Entrada

n = float(input("Insira Valor de N: "))
cont = float(input("Insira Valor de Cont: "))

# Processamneto

while n < cont:
    cont = cont + 1
    print(cont)
    cont = n
    break

# Saída

else:
    print("Fim")