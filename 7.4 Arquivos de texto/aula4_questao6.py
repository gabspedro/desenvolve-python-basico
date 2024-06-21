# Exercício 6
import csv

# Função para verificar se a linha deve ser ignorada devido ao formato
def deve_ignorar_linha(linha):
    # Contando as aspas duplas na linha
    num_aspas = linha.count('"')
    # Se o número de aspas for ímpar, a linha deve ser ignorada
    return num_aspas % 2 != 0

# Lista para armazenar as músicas mais populares de cada ano
top_musicas = []

with open('spotify-2023.csv', 'r', encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # Ignorando o cabeçal
