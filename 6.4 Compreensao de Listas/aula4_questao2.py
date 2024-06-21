import random

vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

frase = str(input("Escreva Uma Frase: "))
print(f"A Frase Escolhida: {frase}")
f_vogais = [l for l in frase if l in vogais]
print(f"Essas são as Vogais Presentes na Frase{sorted(f_vogais)}")
f_consoantes = [l for l in frase if l in consoantes]
print(f"Essas são as Consoantes Presentes na Frase{sorted(f_consoantes)}")