# Exercício 2
# Lendo a frase do arquivo frase.txt
with open('frase.txt', 'r') as file:
    frase = file.read()

# Removendo espaços em branco e caracteres não alfabéticos
palavras = ''.join(char if char.isalpha() else ' ' for char in frase).split()

# Salvando as palavras no arquivo palavras.txt
with open('palavras.txt', 'w') as file:
    for palavra in palavras:
        file.write(palavra + '\n')

# Imprimindo o conteúdo do arquivo palavras.txt
with open('palavras.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)
