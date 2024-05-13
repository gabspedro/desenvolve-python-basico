# Entrada

Classes = input()
Forca   = int(input())
Magia   = int(input())

# Processamento

# A = Força das Classes
# B = Magia das Classes

a = (Classes == 'Mago' and Forca <= 10) or (Classes == 'Guerreiro' and Forca >= 15) or (Classes == 'Arqueiro' and Forca >= 5 <= 15)
b = (Classes == 'Mago' and Magia >= 15) or (Classes == 'Guerreiro' and Forca <= 10) or (Classes == 'Arqueiro' and Magia >= 5 <= 15)

atributo_ok  = a and b

# Saída

print("Os Atributos Estão Ok!" if atributo_ok == True else "Os Atributos Não Estão Ok!")
print("Você Pode Entrar" if a == True and b == True else "Você Não Pode Entrar")
