# Exercício 5
import csv

livros = [
    {"Título": "Dom Casmurro", "Autor": "Machado de Assis", "Ano de publicação": 1899, "Número de páginas": 256},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 128},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1200},
    {"Título": "Harry Potter e a Pedra Filosofal", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 223},
    {"Título": "A Culpa é das Estrelas", "Autor": "John Green", "Ano de publicação": 2012, "Número de páginas": 288},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "A Metamorfose", "Autor": "Franz Kafka", "Ano de publicação": 1915, "Número de páginas": 64},
    {"Título": "O Alquimista", "Autor": "Paulo Coelho", "Ano de publicação": 1988, "Número de páginas": 176},
    {"Título": "Sapiens: Uma Breve História da Humanidade", "Autor": "Yuval Noah Harari", "Ano de publicação": 2011, "Número de páginas": 464}
]

with open('meus_livros.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Título", "Autor", "Ano de publicação", "Número de páginas"])
    writer.writeheader()
    for livro in livros:
        writer.writerow(livro)

print("Arquivo meus_livros.csv criado com sucesso!")