# Entrada

Genero  = input()
Idade   = int(input())
Tempo   = int(input())

# Processamento

# A = Para Mulheres Ter Mais de 60 Anos. Para Homens, 65 Anos
# B = Ou Ter Trabalhando Pelo Menos de 30 Anos
# C = Ou Ter 60 Anos e Trabalhando Pelo Menos 25 Anos

a = (Genero == 'F' and Idade == 65) or (Genero == 'M' and Idade == 65)
b = Tempo > 30
c = Idade >= 60 and Tempo > 25

pode_aposentar = a or b or c

# Saída

print(a, b, c, pode_aposentar)
print("Você Pode Entrar" if a == True or b == True or c == True else "Você Não Pode Aposentar")
