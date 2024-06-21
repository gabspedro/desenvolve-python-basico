# Exercício 1
frase = input("Digite uma frase: ")

# Salvando a frase no arquivo frase.txt
with open('frase.txt', 'w') as file:
    file.write(frase)

# Imprimindo o caminho completo do arquivo salvo
import os
caminho_completo = os.path.abspath('frase.txt')
print(f"Frase salva em {caminho_completo}")
