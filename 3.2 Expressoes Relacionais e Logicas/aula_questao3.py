# Entrada

idade = int(input("Qual Sua Idade? "))
matchs = int(input("Jogou Quantas Partidas? "))
wins = int(input("Já Teve Quantas Vitórias? "))

# Processamento

    # True se todos os dados estiverem dentro das regras
    # Idade entre 16 e 18 anos
    # Ter jogado 3 partidas
    # Ter ganhado 1 partida

pode_entrar = idade > 15 and idade < 19, matchs >=3, wins >= 1

# Saída

print(pode_entrar)