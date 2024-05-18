n = int(input())
cont = 0
soma_coelhos, soma_sapo, soma_ratos = 0, 0, 0

while cont < n:
    quantia = int(input())
    tipo = input()
    print("\n")

    cont += 1

if tipo == 'C':
    soma_coelhos += quantia
elif tipo == 'S':
    soma_sapo += quantia
elif tipo == 'R':
    soma_ratos += quantia

print("Total de Cobaias: ", soma_coelhos + soma_sapo + soma_ratos)
print("Total de Coelhos: ", soma_coelhos/n)
print("Total de Sapos: ",   soma_sapo/n)
print("Total de Ratos: ",   soma_ratos/n)