# Exercício 3
import urllib.request

url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"
filename = "estomago.txt"

# Baixando o arquivo
urllib.request.urlretrieve(url, filename)

# Abrindo o arquivo para leitura
with open(filename, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Imprimindo as primeiras 25 linhas
print("Texto das primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.rstrip())

# Número total de linhas
num_linhas = len(linhas)
print(f"\nNúmero total de linhas: {num_linhas}")

# Linha com maior número de caracteres
maior_linha = max(linhas, key=len).rstrip()
print(f"\nLinha com maior número de caracteres:\n{maior_linha}")

# Contagem de menções aos nomes dos personagens "Nonato" e "Íria"
nome1 = "Nonato"
nome2 = "Íria"
count_nonato = sum(linha.lower().count(nome1.lower()) for linha in linhas)
count_iria = sum(linha.lower().count(nome2.lower()) for linha in linhas)
print(f"\nMenções a '{nome1}' e '{nome2}': {count_nonato + count_iria}")
