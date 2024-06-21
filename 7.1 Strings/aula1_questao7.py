import random

def encrypt(nomes):
    n = random.randint(1, 10)
    encrypted_nomes = []
    for nome in nomes:
        encrypted_nome = ''.join(chr((ord(c) - 33 + n) % 94 + 33) for c in nome)
        encrypted_nomes.append(encrypted_nome)
    return encrypted_nomes, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")