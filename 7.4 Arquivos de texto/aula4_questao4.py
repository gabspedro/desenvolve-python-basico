# Exercício 4 - Jogo da Forca
import random

def imprime_enforcado(erros):
    estagios = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        '''
    ]

    print(estagios[erros])

def escolhe_palavra():
    with open('gabarito_forca.txt', 'r') as file:
        palavras = file.read().splitlines()
    return random.choice(palavras).lower()

def exibe_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra.lower() in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def main():
    palavra = escolhe_palavra()
    letras_corretas = set()
    tentativas = 6
    letras_digitadas = set()

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra:")

    while tentativas > 0:
        exibe_palavra(palavra, letras_corretas)
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").lower()

        if letra in letras_digitadas:
            print(f"Você já tentou a letra '{letra}'. Tente outra.")
            continue
        else:
            letras_digitadas.add(letra)

        if letra in palavra:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Letra incorreta!")
            imprime_enforcado(6 - tentativas)

        if all(letra in letras_corretas for letra in palavra):
            exibe_palavra(palavra, letras_corretas)
            print("Parabéns, você ganhou!")
            break

    if tentativas == 0:
        print(f"Você perdeu! A palavra era '{palavra}'.")

if __name__ == "__main__":
    main()